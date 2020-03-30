from django.forms import forms, ModelForm 
from .models import FFL


class Addffl(ModelForm):
    class Meta:
        model = FFL
        fields ='__all__'
        template_name = 'ffl/templates/addffl_form.html'