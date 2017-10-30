from django.db import models

class Article(models.Model):
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        text = ("%s" % (self.headline))
        return text


class Props(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateField(auto_now=False, auto_now_add=True)


class Comment(models.Model):
    prop = models.ForeignKey(Props, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True)
    body = models.TextField()
    created_date = models.DateField(auto_now=False, auto_now_add=True)


