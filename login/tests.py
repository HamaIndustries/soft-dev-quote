from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse
from rest_framework.test import APIClient
from .views import login_api

from django.contrib.auth.models import User
from profile_mgmt.models import UserInfo
from django.contrib.auth.hashers import make_password


# Create your tests here.

class LoginCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        geto = User(username="geto", password=make_password("1234"))
        geto.save()
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

    def test_login_api(self):
        response = self.client.get('/api/login')
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_request(self):
        url = reverse('login:login_api')
        data = {
            'username' : 'mynewusername',
            'password' : 'anewpassword123'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'The data was received.')

    def test_login_valid_data(self):
        data = {
            'username' : 'geto',
            'password' : '1234',
        }
        response = self.client.post('/api/login', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Login successful', 'session': 'geto'})

    # def test_login_invalid_data(self):
    #     invalid_data = {
    #         'username': 'ausername',
    #         'password': ''
    #     }
    #     response = self.client.post('/api/login', data = invalid_data, format='json')
    #     breakpoint()
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn('password', response.json().get('errors', {}))
    #     self.assertEqual(response.json()['errors']['password'], ['The input is not correct.'])

    def test_login_invalid_data(self):
        invalid_data = {
        'username': '',
        'password': 'apasswordforuser1'
        }
        response = self.client.post('/api/login', data = invalid_data, format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('username', response.json().get('errors', {}))
        self.assertEqual(response.json()['errors']['username'], ['This field is required.'])

    def test_register_valid_data(self):
        data = {
            'username' : 'wewo',
            'password' : '12384',
        }
        response = self.client.post('/api/loginregister', data, format='json')
        self.assertEqual(response.status_code, 200)
