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

class PropForm(ModelForm):
    class Meta:
        model = Props
        fields = ['body']
