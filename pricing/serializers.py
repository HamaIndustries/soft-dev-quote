# Inside your Django app's serializers.py file
from rest_framework import serializers
from .models import FuelQuote

class FuelQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelQuote
        fields = "gallons_requested delivery_address delivery_date suggested_price_per_gallon total_amount_due".split()
