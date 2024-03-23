from django.test import TestCase
from django.urls import reverse
from .models import FuelQuote
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class FuelQuoteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_fuel_quote(self):
        url = reverse('pricing:create_fuel_quote')
        data = {
            'gallons_requested': 100,
            'delivery_address': '123 Main St',
            'delivery_date': '2024-03-24',
            'suggested_price_per_gallon': '2.50',
            'total_amount_due': '250.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FuelQuote.objects.count(), 1)
        fuel_quote = FuelQuote.objects.get()
        self.assertEqual(fuel_quote.gallons_requested, 100)
        self.assertEqual(fuel_quote.delivery_address, '123 Main St')
        

   