import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Serialized
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
