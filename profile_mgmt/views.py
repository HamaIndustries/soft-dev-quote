# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User

from django.shortcuts import render
from .forms import ProfileForm
from .models import UserInfo

import datetime
import json

def profile_mgmt_api(request): 
    try:
        user = User.objects.get(username=request.GET["session"])
    except (KeyError, User.DoesNotExist):
        return JsonResponse({"error": "You are probably not logged in"}, status=403)
    
    if request.method == 'GET':  # handle GET requests
        print("Fetching data from the backend")  
        fields = 'name address1 address2 city state zipcode'.split()
        try:
            data = UserInfo.objects.values(*fields).get(user=user)
        except UserInfo.DoesNotExist:
            data = {k: ' ' for k in fields}

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
            user_profile = UserInfo.objects.update_or_create(
                user=user,
                defaults = dict(
                    name=name,
                    address1=address1,
                    address2=address2,
                    city=city,
                    state=state,
                    zipcode=zipcode
                )
            )

            return JsonResponse({'message': 'Data received successfully'}) # send json data to frontend

        else:
            errors = dict(form.errors.items())
            return JsonResponse({'errors': errors}, status=400)
    
    

