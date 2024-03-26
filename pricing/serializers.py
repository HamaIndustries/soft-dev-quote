# Inside your Django app's serializers.py file
from rest_framework import serializers
from .models import FuelQuote

class FuelQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelQuote
        fields = '__all__'
