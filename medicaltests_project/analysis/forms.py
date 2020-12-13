from django.forms import ModelForm
from .models import *

class ResultForm(ModelForm):
    class Meta:
        model=Result
        fields='__all__'
