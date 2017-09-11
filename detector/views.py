from django.shortcuts import render
from .models import Article, Props
from .forms import PropForm

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
