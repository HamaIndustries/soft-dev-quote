from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest
from .forms import LoginForm
from .models import Username
from django.contrib.auth import authenticate, login, logout 
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.


def login_api(request):

    if request.method == 'GET':
        data = {
            'username': 'myusername',
            'password': 'mypassword123'
        }
        return JsonResponse(data)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')
        
        loginform = LoginForm(data)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            
            
            user = authenticate(request, username=username, password=password)
          

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful'})
            else:
                 # Debug information
                try:
                    user = User.objects.get(username=username)
                    print(f"User {user.username} exists but authentication failed.")

                    if password == user.password:
                        print("password exists")
                    else:
                        print("failed")
                except User.DoesNotExist:
                    print(f"User with username {username} does not exist.")
                
                return JsonResponse({'error': 'Invalid credentials'})
        

    return JsonResponse({'message': 'The data was received.'})

        
        
def registerAccount(request):

    if request.method == 'GET':
        data = {
            'username': 'patrick',
            'password': 'dagoat123'
        }
        return JsonResponse(data)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            
        except json.JSONDecodeError:
            return HttpResponseBadRequest('The format was not correct.')
        
        loginform = LoginForm(data)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = make_password(loginform.cleaned_data['password'])

             # Create a new user
            user = User.objects.create(username=username, password=password)

            return JsonResponse({'message': 'The data was received.'})

        else:
            errors = dict(loginform.errors.items())
            return JsonResponse({'errors': errors}, status=400)
        

def logoutUser(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})
        


#@api_view(['POST'])

#def loginuser(request):
#    user = get_object_or_404(User, username=request.data['username'])
#    if not user.check_password(request.data['password']):
#        return Response({"detail:" "Not found."}, status=status.HTTP_404_NOT_FOUND)
#    token, newcreate = Token.objects.get_or_create(user=user)
#    serializer = UserSerializer(instance=user)
#    return Response({"token": token.key, "user": serializer.data})
