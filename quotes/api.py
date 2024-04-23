import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
import json

from django.http import HttpRequest, HttpResponse, response

from pricing.models import FuelQuote

def login_api(request: HttpRequest):
    """
    Accepts JSON object containing username and (hashed) password

    responds with success and session info if valid.
    """
    pass

def registration_api(request: HttpRequest):
    """
    Accepts JSON object containing registration info

    responds with success if data is valid.
    """

def quote_history_api(request: HttpRequest):
    data = { "history" : [] }
    if session := request.GET["session"]:
        try:
            user = User.objects.get(username=session)
        except User.DoesNotExist:
            return JsonResponse({"error": "you are not logged in"}, status=400)
        
        data["history"] = list(
            FuelQuote.objects.values().filter(owner=user)
        )
    return JsonResponse(data, status=200)
    

def quote_form_api(request: HttpRequest):
    """
    Accepts JSON object describing quote request, and responds with success if valid.
    Should provide an "id" field that is 0 if creating a new form, and >0 if editing an existing one with that id.
    there should also be a delete method. (CRUD)
    """

    try:
        data = json.loads(request.body)
        print("Received json content:")
        print(data)

        if "id" in data and data["id"] == 0:
            data["id"] = 69 # pretend the database created a new form
        return HttpResponse(json.dumps(data), content_type="application/json", status=200) # pretend database responds with modified accepted data
    except json.JSONDecodeError:
        print(f"failed to parse JSON data: {request.body}")
        raise