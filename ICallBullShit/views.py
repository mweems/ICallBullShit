from django.shortcuts import render, redirect
from detector.models import Article


def admin(request):
    article_list = Article.objects.all()
    return render(request, 'detector/index.html', {'article_list': article_list})