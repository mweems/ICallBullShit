from django.conf.urls import url

from . import views

app_name = 'detector'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail' )
]