from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

import datetime

"""
def current_datetime(request):
    now = datetime.datetime.now()
    data = {'current_datetime': now}
    return JsonResponse(data)
"""


def profile_mgmt_api(request):
    
    if request.method == 'GET':  # handle GET requests
        print("Fetching data from the backend")  
      
        data = {
            'name': 'Geto Suguru',
            'address1': '1234 Tokyo Str',
            'address2': '',
            'city': 'Tokyo',
            'state': 'JP',
            'zipcode': '12345',
        }
        return JsonResponse(data)
    
    elif request.method == 'POST':  # Handle POST requests
        data = {'message': 'Data received successfully'}
        return JsonResponse(data)
    

