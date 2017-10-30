from django.conf.urls import url

from . import views

app_name = 'detector'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_article/$', views.create_article, name='create_article'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail' ),
    url(r'^discussion/(?P<prop_id>[0-9]+)/$', views.discussion, name='discussion'),
]