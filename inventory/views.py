from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . models import Inventory, Orders, Consumables
from . forms import AddInv, AddOrders, AddConsumables


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class StaffIndex(TemplateView):
    template_name = 'staffindex.html'

class AddInvView(CreateView):
    model = Inventory 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addinv_form.html'
    success_url = 'list'

class AddOrderView(CreateView):
    model = Orders 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addorders_form.html'
    success_url = 'orderlist'

class OrderDelete(DeleteView):
    model = Orders
    success_url = 'orderlist'
    template_name = 'order_confirm_delete.html'


class AddConsumables(CreateView):
    model = Consumables 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addconsumables_form.html'
    success_url = 'consumables'

class UpdateInvView(UpdateView):
    model = Inventory
    success_url = 'list'
    template_name = 'invupdate.html'
    fields = '__all__'
    context_object_name = 'inv'

class UpdateOrderView(UpdateView):
    model = Orders
    success_url = 'orderlist'
    template_name = 'orderupdate.html'
    fields = '__all__'
    context_object_name = 'orders'

class UpdateConsumables(UpdateView):
    model = Consumables
    success_url = 'consumables'
    template_name = 'consumablesupdate.html'
    fields = '__all__'
    context_object_name = 'objects'
    

class InvListView(ListView):
    model = Inventory
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class StaffListView(ListView):
    model = Inventory
    template_name = "staff_list.html"

class OrderListView(ListView):
    model = Orders
    template_name = "orders_list.html"

class ConsumablesView(ListView):
    model = Consumables
    paginate_by =10 
    template_name = "consumables_list.html"
    

    

    