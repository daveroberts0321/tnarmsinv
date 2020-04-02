from django.shortcuts import render
import requests
import bigcommerce

# Create your views here.

api = bigcommerce.api.BigcommerceApi(
    client_id='5zu8djlu07xick65yf3vgs3urf6oxm1', 
    store_hash='e6d39bb59d02e87f66844799d28949d1fee712c7d18ca32daaa3f3dcd5c4c2cb', 
    access_token='993u0lwo671cywg6oxuuhn53elkw28p',
    rate_limiting_management= {'min_requests_remaining':2,'wait':True,'callback_function':None}
    )

