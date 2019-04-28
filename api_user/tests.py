import requests_mock
from rest_framework.test import APITestCase
import json

from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)

class ApiUserRedirectTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'user_account_id':'1'
        }

        self.invalid_payload = {
            'user_account_id':''
        }
    
    @requests_mock.Mocker(kw='mock')
    def test_get_user(self, **kwargs):
        id = self.valid_payload
        api_url = '/get_user/'
        request_url = 'http://api-monitoria:8001/user/1/'
        status = HTTP_200_OK
        data = {"Teste": "teste"}

        kwargs['mock'].get(request_url, text=json.dumps(data))

        response = self.client.post(api_url,id)

        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data['Teste'], "teste")

    def test_error_get_user(self, **kwargs):
        id = self.invalid_payload
        api_url = '/get_user/'
        status = HTTP_500_INTERNAL_SERVER_ERROR
        data = {'error': 'Error no servidor'}

        response = self.client.post(api_url, id)
        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data, data)