from django.db import models

class Article(models.Model):
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)


class props(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
