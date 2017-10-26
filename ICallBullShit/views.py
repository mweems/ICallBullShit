from django.shortcuts import render, redirect
from detector.models import Article


def admin(request):
    article_list = Article.objects.all()
    return render(request, 'admin/admin.html', {'article_list': article_list})

def remove(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    article_list = Article.objects.all()
    return redirect('admin')

