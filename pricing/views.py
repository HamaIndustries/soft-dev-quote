from django.shortcuts import render
from django.contrib.auth.models  import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FuelQuote
from .serializers import FuelQuoteSerializer
from .serializers import field_names

@api_view(['POST'])
def create_fuel_quote(request):
    data = dict(request.data)
    if all([field in data for field in field_names]):    
        for pricek in ["suggested_price_per_gallon", "total_amount_due"]:
            data[pricek] = round(float(data[pricek]), 2)
    serializer = FuelQuoteSerializer(data=data)
    try:
        user = User.objects.get(username=request.GET["session"])
    except User.DoesNotExist:
        return Response("error: user does not exist", status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response("error: missing session key", status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        FuelQuote(owner=user, **serializer.validated_data).save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
