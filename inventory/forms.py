# users/forms.py
from django.forms import forms, ModelForm 
from .models import Inventory

class AddInv(ModelForm):
    class Meta:
        model = Inventory
        fields ='__all__'
        template_name = 'addinv_form.html'


