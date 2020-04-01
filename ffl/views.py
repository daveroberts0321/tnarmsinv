
import csv, io
from django.shortcuts import render
from django.db.models import Q
from .models import FFL
from .forms import Addffl
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
class FFLIndex(LoginRequiredMixin, ListView):
    template_name = 'ffl/fflindex.html'
    paginate_by = 20
    model = FFL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ffl'] = FFL.objects.all()
        #context['fflcount'] = FFL.objects.all.count()        
        return context

    def listing(request):
        ffl_list = FFL.objects.all()
        paginator = Paginator(ffl_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'ffl/fflindex.html', {'page_obj': page_obj})

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

def FFLUpload(request):
    # declaring template
    template = "ffl/ffl_upload.html"
    data = FFL.objects.all()
# prompt is a context variable that can have different values      depending on their context
    #prompt = {
        #'order': 'Order of the CSV should be SERIAL NUMBER, MODEL TYPE, COLOR, NOTES'
       # 'Serialized':data   
          #    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = FFL.objects.update_or_create(
            fflcompanyname=column[0],
            fflnumber=column[1],
            fflcity=column[2],
            fflstate=column[3],
            fflexp=column[4],            
            fflmailaddress=column[5],                  
            fflcfd=column[6],
            fflzipcode=column[7],
            notes=column[8]
            )
    context = {}
    return render(request, template, context)