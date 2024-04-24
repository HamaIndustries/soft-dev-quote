from django.test import TestCase
from django.urls import reverse

from profile_mgmt.models import UserInfo
from .models import FuelQuote
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class FuelQuoteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        geto = User(username="geto", password="1234")
        geto.save()
        self.geto = geto
        UserInfo.objects.get_or_create(
            user=geto,
            defaults={
                'name': 'Geto Suguru',
                'address1': '1234 Tokyo Str',
                'address2': '',
                'city': 'Tokyo',
                'state': 'JP',
                'zipcode': '12345',
            }
        )

    def test_create_fuel_quote(self):
        url = reverse('pricing:create_fuel_quote')  + '?session=geto'
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

    def test_create_fuel_quote_invalid_data(self):
        url = reverse('pricing:create_fuel_quote')  + '?session=geto'
        invalid_data = {
            'gallons_requested': '',
            'delivery_address': '',
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(FuelQuote.objects.count(), 0)
    
    def test_create_fuel_quote_duplicate(self):
        url = reverse('pricing:create_fuel_quote')  + '?session=geto'
        data = {
            'gallons_requested': 200,
            'delivery_address': '456 Main St',
            'delivery_date': '2024-04-24',
            'suggested_price_per_gallon': '3.50',
            'total_amount_due': '700.00'
        }
        self.client.post(url, data, format='json')
        duplicate_data = data
        response = self.client.post(url, duplicate_data, format='json')
        # breakpoint()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_fuel_quote_invalid_field_values(self):
        url = reverse('pricing:create_fuel_quote') + '?session=geto'
        data = {
            'gallons_requested': "wa wa",  
            'delivery_address': '789 Main St',
            'delivery_date': '2020-01-01',  
            'suggested_price_per_gallon': '-1.00',  
            'total_amount_due': '0.00'  
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

    def test_create_fuel_quote_unauthenticated(self):
        url = reverse('pricing:create_fuel_quote')
        data = {
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  

    def test_create_fuel_quote_authenticated(self):
        test_user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=test_user)
        url = reverse('pricing:create_fuel_quote') + '?session=testuser'
        data = {
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.client.force_authenticate(user=None)
   
    def test_retrieve_fuel_quote(self):
        create_url = reverse('pricing:create_fuel_quote') + '?session=geto'
        data = {
        }
        create_response = self.client.post(create_url, data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_400_BAD_REQUEST)
   