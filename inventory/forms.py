# users/forms.py
from django.forms import forms, ModelForm 
from .models import Inventory, Orders, Consumables

class AddInv(ModelForm):
    class Meta:
        model = Inventory
        fields ='__all__'
        template_name = 'addinv_form.html'

class AddOrders(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        template_name = 'addorders_form.html'

class AddConsumables(ModelForm):
    class Meta:
        model = Consumables
        fields = '__all__'
        template_name = 'addconsumables_form.html'
