from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . models import Inventory
from . forms import AddInv


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

class UpdateInvView(UpdateView):
    model = Inventory
    success_url = 'list'
    template_name = 'invupdate.html'
    fields = '__all__'
    context_object_name = 'inv'
    

class InvListView(ListView):
    model = Inventory
    paginate_by = 10  # if pagination is desired
    template_name = "inventory_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class StaffListView(ListView):
    model = Inventory
    paginate_by = 10  # if pagination is desired
    template_name = "staff_list.html"

    