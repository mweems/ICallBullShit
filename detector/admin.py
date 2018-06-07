from django.contrib import admin

from .models import Article, Props, Comment

admin.site.register(Article)
admin.site.register(Props)
admin.site.register(Comment)
