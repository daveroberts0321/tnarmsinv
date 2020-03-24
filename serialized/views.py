import csv, io
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Serialized
from .forms import AddSerialized
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
# one parameter named request
def SerializedUpload(request):
    # declaring template
    template = "serialized_upload.html"
    data = Serialized.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be serial Number, date aquired, date deposed, order number',
        'Serialized': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Serialized.objects.update_or_create(
            serialnumber=column[0],
            dateaquired=column[1],
            datedeposed=column[2],
            ordernumber=column[3],
            )
    context = {}
    return render(request, template, context)

class AddSerialized(CreateView):
    model = Serialized
    fields = '__all__'
    query_pk_and_slug = True
    template_name = 'serialized/addserialized_form.html'
    success_url = reverse_lazy('serialized:serializedlist')

class SerializedListView(ListView):
    '''serialized inventory list view'''
    model = Serialized
    template_name = 'serialized/staff_serialized.html'


class SerializedDetailView(DetailView):
    '''Serialized inventory Detail View'''
    model = Serialized

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context