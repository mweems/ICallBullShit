from django.forms import ModelForm
from .models import Props, Article, Comment
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = []
        widgets = {
            'body': forms.TextInput(),
            'pub_date': forms.DateInput({'type': 'date'})
        }
        labels = {
            'body':'Article URL'
        }

class PropForm(ModelForm):
    class Meta:
        model = Props
        fields = ['body']
        widgets = {
            'body': forms.TextInput(),
        }
        labels = {
            'body': "Add Propoganda"
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput()
        }
        labels = {
            'text': 'Add Comment'
        }
