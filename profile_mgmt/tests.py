from django.test import TestCase, Client
from django.urls import reverse, resolve
from rest_framework.test import APIClient

from .views import profile_mgmt_api

# Create your tests here.
class ProfileManagementTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_profile_mgmt_api(self):
        response = self.client.get('/api/profile_mgmt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_request(self): # test if dummy data matches
        response = self.client.get('/api/profile_mgmt')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'name': 'Geto Suguru',
                'address1': '1234 Tokyo Str',
                'address2': '',
                'city': 'Tokyo',
                'state': 'JP',
                'zipcode': '12345',
            }
        )

    def test_post_request(self):
        url = reverse('profile_mgmt:profile_mgmt_api') 
        data = {
            'name': 'John Doe',
            'address1': '123 Main St',
            'address2': '',
            'city': 'Anytown',
            'state': 'CA',
            'zipcode': '12345'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Data received successfully')


    def test_valid_data(self):
        data = {
            'name': 'Gojo Satoru',
            'address1': '123 Main St',
            'address2': '',
            'city': 'Anytown',
            'state': 'CA',
            'zipcode': "12345",
        }
        response = self.client.post('/api/profile_mgmt', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Data received successfully'})


    
    def test_invalid_data_missing_fields(self):
        invalid_data = {
            'name': 'Gojo Satoru',
            'address1': '',  
            'address2': '',
            'city': 'Anytown',
            'state': 'CA',
            'zipcode': '',  
        }
        response = self.client.post('/api/profile_mgmt', data=invalid_data, format="json")
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('address1', response.json().get('errors', {}))
        self.assertIn('zipcode', response.json().get('errors', {}))

    def test_invalid_data_zipcode_length(self):
        invalid_data = {
            'name': 'Gojo Satoru',
            'address1': '123 Main St',
            'address2': '',
            'city': 'Anytown',
            'state': 'CA',
            'zipcode': '1234',  # zipcode does not satisfy length
        }
        response = self.client.post('/api/profile_mgmt', data=invalid_data, format="json")
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('zipcode', response.json().get('errors', {}))
        self.assertEqual(response.json()['errors']['zipcode'], ['Ensure this value has at least 5 characters (it has 4).'])

    def test_unexpected_input(self):
        invalid_data = {
            'name': 12345,  # integer value instead of string
            'address1': '123 Main St',
            'address2': '',
            'city': 'Anytown',
            'state': 'CA',
            'zipcode': '12345',
        }
        response = self.client.post('/api/profile_mgmt', data=invalid_data, format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.json().get('errors', {}))
        self.assertEqual(response.json()['errors']['name'], ['Enter a valid value.'])
    
        
        

   


    


