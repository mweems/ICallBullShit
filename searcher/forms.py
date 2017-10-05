from detector.models import Article
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = []
        widgets = {
            'body': forms.TextInput(),
            'pub_date': AdminDateWidget()
        }
