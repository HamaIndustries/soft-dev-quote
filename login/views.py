from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.


def login_api(request):

    if request.method == 'GET':
        data = {
            'username': 'myusername',
            'password': 'mypassword123'
        }
        return JsonResponse(data)
    
    elif request.method == 'POST':
        data = {'message': 'Success'}
        return JsonResponse(data)

#@api_view(['POST'])

#def loginuser(request):
#    user = get_object_or_404(User, username=request.data['username'])
#    if not user.check_password(request.data['password']):
#        return Response({"detail:" "Not found."}, status=status.HTTP_404_NOT_FOUND)
#    token, newcreate = Token.objects.get_or_create(user=user)
#    serializer = UserSerializer(instance=user)
#    return Response({"token": token.key, "user": serializer.data})
