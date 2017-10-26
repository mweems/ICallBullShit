"""ICallBullShit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import admin, remove_article, remove_prop

urlpatterns = [
    url(r'^admin/', admin, name='admin'),
    url(r'^remove_article/(?P<article_id>[0-9]+)/$', remove_article, name='remove_article'),
    url(r'^remove_prop/(?P<prop_id>[0-9]+)/$', remove_prop, name='remove_prop'),
    url(r'^detector/', include('detector.urls')),
]
