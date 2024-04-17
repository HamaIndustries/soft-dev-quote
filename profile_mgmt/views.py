from django.shortcuts import render
from .forms import ProfileForm
from .models import UserInfo

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest

import datetime
import json



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
        try:
            data = json.loads(request.body)
          
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')
        
        form = ProfileForm(data)
        if form.is_valid():
            # Processing valid data
            name = form.cleaned_data['name']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

             # Save data to the database
            user_profile = UserInfo.objects.create(
                name=name,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                zipcode=zipcode
            )


            return JsonResponse({'message': 'Data received successfully'}) # send json data to frontend

        else:
            errors = dict(form.errors.items())
            return JsonResponse({'errors': errors}, status=400)
    
    

