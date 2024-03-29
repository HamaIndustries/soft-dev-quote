from django.test import TestCase, Client
from django.urls import reverse, resolve

from .views import profile_mgmt_api

# Create your tests here.
class ProfileManagementTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_profile_mgmt_api(self):
        response = self.client.get('/api/profile_mgmt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_valid_data(self):
        data = {
            'name': 'Gojo Satoru',
            'address1': '123 Main St',
            'address2': '',
            'city': 'Anytown',
            'state': 'CA',
            'zipcode': '12345',
        }
        response = self.client.post('/api/profile_mgmt', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Data received successfully'})

    def test_invalid_data(self):
        invalid_data = {
            'name': 'Gojo Satoru',
            'address1': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            # 'zipcode' is missing, which should cause the request to be invalid
        }
        response = self.client.post('/api/profile_mgmt', data=invalid_data)
    
        self.assertEqual(response.status_code, 400)
        self.assertIn('zipcode', response.json().get('errors', {}))
        self.assertEqual(response.json()['errors']['zipcode'], ['This field is required.'])


    def test_invalid_data_missing_fields(self):
        invalid_data = {
            'name': 'Gojo Satoru',
            'city': 'Anytown',
            'state': 'CA',
        }
        response = self.client.post('/api/profile_mgmt', data=invalid_data)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('address1', response.json().get('errors', {}))
        self.assertIn('zipcode', response.json().get('errors', {}))


    


