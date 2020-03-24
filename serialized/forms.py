from django.forms import forms, ModelForm 
from .models import Serialized

class AddSerialized(ModelForm):
    class Meta:
        model = Serialized
        fields ='__all__'
        template_name = 'addserialized_form.html'