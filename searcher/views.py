from django.shortcuts import render
import justext
import requests
from .forms import ArticleForm
from detector.models import Article

def index(request):

    form = ArticleForm()
    if request.method == 'POST':
        data = ArticleForm(request.POST)
        print(data['headline'])
        response = requests.get(data.cleaned_data['body'])
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        if data.is_valid():
            Article.objects.create(
                publisher=data.cleaned_data['publisher'],
                author=data.cleaned_data['author'],
                headline=data.cleaned_data['headline'],
                body=paragraphs,
                pub_date=data.cleaned_data['pub_date']
            )
        return render(request, 'searcher/searcher.html', {'form': form, 'message': 'Successfully created Article'})
    return render(request, 'searcher/searcher.html', {'form': form})

