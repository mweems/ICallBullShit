from django.forms import ModelForm
from .models import Props, Article
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = []
        widgets = {
            'body': forms.TextInput()
        }
        labels = {
            'body':'Article URL'
        }

class PropForm(ModelForm):
    class Meta:
        model = Props
        fields = ['body']
