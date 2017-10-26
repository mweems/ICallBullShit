from django.shortcuts import render, redirect
from detector.models import Article, Props


def admin(request):
    articles = Article.objects.all()

    return render(request, 'admin/admin.html', {'articles': articles})

def remove_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('admin')

def remove_prop(request, prop_id):
    prop = Props.objects.get(pk=prop_id)
    prop.delete()
    return redirect('admin')

