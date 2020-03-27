from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . models import Inventory, Orders, Consumables, Supplier
from . forms import AddInv, AddOrders, AddConsumables, AddSupplier


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class StaffIndex(TemplateView):
    template_name = 'staffindex.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consumables'] = Consumables.objects.all()
        context['object_list'] = Inventory.objects.all()
        context['orders'] = Orders.objects.all()
        return context

class AddInvView(LoginRequiredMixin, CreateView):
    model = Inventory 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addinv_form.html'
    success_url = 'list'

class AddSupplier(LoginRequiredMixin, CreateView):
    model = Supplier
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addsupplier_form.html'
    success_url = 'supplierlist'

class AddOrderView(LoginRequiredMixin, CreateView):
    model = Orders 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addorders_form.html'
    success_url = 'orderlist'

class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Orders
    success_url = 'orderlist'
    template_name = 'order_confirm_delete.html'

class SupplierDelete(LoginRequiredMixin, DeleteView):
    model = Orders
    success_url = 'supplierslist'
    template_name = 'supplier_confirm_delete.html'


class AddConsumables(LoginRequiredMixin, CreateView):
    model = Consumables 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'addconsumables_form.html'
    success_url = 'consumables'

class UpdateInvView(LoginRequiredMixin, UpdateView):
    model = Inventory
    success_url = 'list'
    template_name = 'invupdate.html'
    fields = '__all__'
    context_object_name = 'inv'

class UpdateSupplierView(LoginRequiredMixin, UpdateView):
    model = Supplier
    success_url = 'supplierlist'
    template_name = 'updatesupplier.html'
    fields = '__all__'
    context_object_name = 'supplier'

class UpdateOrderView(LoginRequiredMixin, UpdateView):
    model = Orders
    success_url = 'orderlist'
    template_name = 'orderupdate.html'
    fields = '__all__'
    context_object_name = 'orders'

class UpdateConsumables(LoginRequiredMixin, UpdateView):
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

class StaffListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = "staff_list.html"

class AdvantageList(LoginRequiredMixin, ListView):
    model = Orders
    template_name = "advantage_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consumables'] = Consumables.objects.all()
        context['object_list'] = Inventory.objects.all()
        context['orders'] = Orders.objects.all()
        return context

class OrderListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = "orders_list.html"

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = "supplierslist.html"
    context_object_name = 'supplier'

class ConsumablesView(LoginRequiredMixin, ListView):
    model = Consumables
    paginate_by =10 
    template_name = "consumables_list.html"
    

    

    