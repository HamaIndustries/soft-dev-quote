from django.shortcuts import render
# Inside your Django app's views.py file
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FuelQuote
from .serializers import FuelQuoteSerializer

@api_view(['POST'])
def create_fuel_quote(request):
    print("wwawawawawwa")
    serializer = FuelQuoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
