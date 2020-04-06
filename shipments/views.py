import io, csv, request
import bigcommerce 
from django.shortcuts import render



# Create your views here.
ACCESS_TOKEN = your_access_token
CLIENT_ID = your_client_id
STORE_HASH = your_store_hash

api = bigcommerce.api.BigcommerceApi(
    client_id='5zu8djlu07xick65yf3vgs3urf6oxm1', 
    store_hash='e6d39bb59d02e87f66844799d28949d1fee712c7d18ca32daaa3f3dcd5c4c2cb', 
    access_token='993u0lwo671cywg6oxuuhn53elkw28p',
    rate_limiting_management= {'min_requests_remaining':2,'wait':True,'callback_function':None}
    )

def GetOrders(request):
    response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSqTOJYTifN_ItVtrTATp1v4zvIWoRtLkiPDntQKrD5SbAKtfy_P94RKJLAZX0J6xtLTse_Fdxsx5a1/pub?gid=1403077119&single=true&output=csv')
    column = response.csv()
    return render(request, 'shipments/rawlist.html', {
        'ordernumber':column[0],
        'lastname':column[1],
        'firstname':column[2]
    })

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
            gunmasterid=column[1],
            modeltype=column[2],
            color=column[3],
            dateaquired=column[4],
            notes=column[5],
            )
    context = {}
    return render(request, template, context)