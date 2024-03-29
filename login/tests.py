from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse

from .views import login_api

# Create your tests here.

class LoginCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_api(self):
        response = self.client.get('/api/login')
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_valid_data(self):
        data = {
            'username': 'newusername',
            'password': 'thisisthenewpassword1234'
        }
        response = self.client.post('api/login', data = data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Success'})

    def test_login_invalid_data(self):
        invalid_data = {
            'username': 'ausername',
            'password': ''
        }
        response = self.client.post('api/login', data = invalid_data)
        self.assertEqual(response.status_code,400)
        self.assertIn('password', response.json().get('errors', {}))
        self.assertEqual(response.json()['errors']['password']['The input is not correct.'])

    def test_login_invalid_data(self):
        invalid_data = {
        'username': '',
        'password': 'apasswordforuser1'
        }
        response = self.client.post('api/login', data = invalid_data)
        self.assertEqual(response.status_code,400)
        self.assertIn('username', response.json().get('errors', {}))
        self.assertEqual(response.json()['errors']['username']['The input is not correct.'])



    