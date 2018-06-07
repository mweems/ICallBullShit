from django.shortcuts import render, redirect
from .models import Article, Props
from .forms import PropForm, ArticleForm, CommentForm
import requests
import justext


def index(request):
    articles = Article.objects.all()
    return render(request, 'detector/index.html', {'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == "POST":
        form = PropForm(request.POST)
        body = form['body'].value()
        if form.is_valid():
            Props.objects.create(article=article, body=body)

    form = PropForm()
    return render(request, 'detector/detail.html', {'article': article, 'form': form})

def discussion(request, prop_id):
    prop = Props.objects.get(pk=prop_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        text = form['text'].value()
        if form.is_valid():
            Comment.objects.create(prop=prop, text=text)

    form = CommentForm()
    return render(request, 'discussion/detail.html', {'prop': prop, 'form': form})



def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        response = requests.get(form['body'].value())
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        if form.is_valid():
            publisher = form['publisher'].value()
            body = ''
            for paragraph in paragraphs:
                if publisher in paragraph.text:
                    text = paragraph.text.replace(publisher, 'News Source')
                else:
                    text = paragraph.text
                if not paragraph.is_boilerplate:
                    body += text
            Article.objects.create(
                publisher=form['publisher'].value(),
                author=form['author'].value(),
                headline=form['headline'].value(),
                body=body,
                pub_date=form['pub_date'].value()
            )
        return redirect('/detector')
    return render(request, 'searcher/create_article.html', {'form': form})
