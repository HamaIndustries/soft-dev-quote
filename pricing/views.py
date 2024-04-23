from django.shortcuts import render
from django.contrib.auth.models  import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FuelQuote
from .serializers import FuelQuoteSerializer

@api_view(['POST'])
def create_fuel_quote(request):
    data = dict(request.data)
    for pricek in ["suggested_price_per_gallon", "total_amount_due"]:
        data[pricek] = round(data[pricek], 2)
    serializer = FuelQuoteSerializer(data=data)
    user = User.objects.get(username=request.GET["session"])
    if serializer.is_valid():
        FuelQuote(owner=user, **serializer.validated_data).save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
