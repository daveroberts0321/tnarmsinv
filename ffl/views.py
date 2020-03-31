
from django.shortcuts import render
from django.db.models import Q
from .models import FFL
from .forms import Addffl
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
class FFLIndex(LoginRequiredMixin, TemplateView):
    template_name = 'ffl/fflindex.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ffl'] = FFL.objects.all()
        #context['fflcount'] = FFL.objects.all.count()        
        return context

class FFLDetail(LoginRequiredMixin, DetailView):
    model = FFL
    template_name = 'ffl/ffl_detail.html'


class AddFFL(LoginRequiredMixin, CreateView):
    model = FFL 
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'ffl/addffl_form.html'
    success_url = reverse_lazy('ffl:fflindex')

class UpdateFFL(LoginRequiredMixin, UpdateView):
    model = FFL
    success_url = 'ffl:fflindex'
    template_name = 'ffl/updateffl.html'
    fields = '__all__'
    
class SearchFFL(ListView):
    model = FFL
    template_name = 'ffl/search_results.html'
    paginate_by = 20

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = FFL.objects.filter(
            Q(fflcompanyname__icontains=query) | Q(fflnumber__icontains=query) | Q(fflmailaddress__icontains=query)
        )
        return object_list

