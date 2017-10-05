from django.shortcuts import render, redirect
from .models import Article, Props
from .forms import PropForm, ArticleForm
import requests
import justext

def index(request):
    article_list = Article.objects.all()
    return render(request, 'detector/index.html', {'article_list': article_list})

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == "POST":
        form = PropForm(request.POST)
        if form.is_valid():
            Props.objects.create(article=article, body=form)

    form = PropForm()
    return render(request, 'detector/detail.html', {'article': article, 'form': form})

def search(request):
    form = ArticleForm()
    if request.method == 'POST':
        data = ArticleForm(request.POST)

        response = requests.get(data['body'].value())
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        if data.is_valid():
            publisher = data['publisher'].value()
            body = ''
            for paragraph in paragraphs:
                if publisher in paragraph.text:
                    text = paragraph.text.replace(publisher, 'News Source')
                else:
                    text = paragraph.text
                if not paragraph.is_boilerplate:
                    body += text
            Article.objects.create(
                publisher=publisher,
                author=data['author'].value(),
                headline=data['headline'].value(),
                body=body,
                pub_date=data['pub_date'].value()
            )
        return render(request, 'searcher/searcher.html', {'form': form, 'message': 'Successfully created Article'})
    return render(request, 'searcher/searcher.html', {'form': form})