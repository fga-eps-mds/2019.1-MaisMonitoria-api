from rest_framework.test import APITestCase
from api_gateway.views import all_tutoring
from rest_framework import status 
import firebase_admin
import requests_mock
import json
import mock

# from rest_framework.status import (
#     HTTP_403_FORBIDDEN,
#     HTTP_200_OK,
#     HTTP_404_NOT_FOUND,
#     HTTP_400_BAD_REQUEST,
#     HTTP_500_INTERNAL_SERVER_ERROR
# )

class ApiUserRedirectTests(APITestCase):
    def setUp(self):
        self.id={
            'id': '1'
        }
        self.valid_payload = {
             'access_token': '123'

        }

        self.invalid_payload = {
            'access_token':''
        }
   
    @mock.patch('firebase_admin.auth.verify_id_token', mock.Mock(return_value={ 'uid': '1','id':'1'}))
    @mock.patch('api.utils.verify_auth', mock.Mock(return_value={ 'id':'1' }))
    @requests_mock.Mocker(kw='mock')
    def test_get_user(self, **kwargs):
        request_id = self.valid_payload
        api_url = '/get_user/'
        request_url = 'http://api-monitoria:8001/user/1'
        request_status = status.HTTP_200_OK
        data = {"Teste": "teste"}

        kwargs['mock'].get(request_url, text=json.dumps(data))

        response = self.client.post(api_url,request_id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['Teste'], "teste")

    def test_error_get_user(self, **kwargs):
        request_id = self.invalid_payload
        api_url = '/get_user/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        response = self.client.post(api_url, request_id )
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)