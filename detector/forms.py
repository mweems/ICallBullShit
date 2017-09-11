from django.forms import ModelForm
from .models import Props

class PropForm(ModelForm):

    class Meta:
        model = Props
        fields = ['body']
