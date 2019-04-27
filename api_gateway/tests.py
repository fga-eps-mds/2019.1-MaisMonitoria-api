from api_gateway.views import all_tutoring
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

class MonitoringRedirectTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'id_tutoring_session': '1'
        }

    #     self.invalid_payload = {
    #         'name': ''
    #     }
    
    @requests_mock.Mocker(kw='mock')
    def test_all_tutoring(self, **kwargs):
        api_url = '/all_tutoring/'
        request_url = 'http://api-monitoria:8001/tutoring/'
        status = HTTP_200_OK
        data = {"Teste": "teste"}

        kwargs['mock'].get(request_url, text=json.dumps(data))

        response = self.client.get(api_url)

        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data['Teste'], "teste")

    def test_error_all_tutoring(self, **kwargs):
        api_url = '/all_tutoring/'
        status = HTTP_500_INTERNAL_SERVER_ERROR
        data = {'error': 'Error no servidor'}

        response = self.client.get(api_url)

        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data, data)

    @requests_mock.Mocker(kw='mock')
    def test_get_tutoring(self, **kwargs):
        id = self.valid_payload
        api_url = '/get_tutoring/'
        request_url = 'http://api-monitoria:8001/tutoring/1/'

        status = HTTP_200_OK
        data = {'Teste': 'teste'}
        kwargs['mock'].get(request_url,text = json.dumps(data))

        response = self.client.post(api_url,id)
        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data['Teste'] ,'teste'  )

    def teste_error_get_tutoring(self, **kwargs):
        id = self.valid_payload
        api_url = '/get_tutoring/'

        status = HTTP_500_INTERNAL_SERVER_ERROR
        data = {'error': 'Error no servidor'} 
        response = self.client.post(api_url,id)
        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data ,data  )
        


    # @requests_mock.Mocker(kw='mock')
    # def test_all_tutoring(self, **kwargs):
    #     api_url = '/tutoring/'
    #     request_url = 'http://api-monitoria:8001/tutoring/'
    #     status = HTTP_200_OK
    #     data = {"Teste": "teste"}

    #     kwargs['mock'].get(request_url, text=json.dumps(data))

    #     response = self.client.get(api_url)

    #     self.assertEqual(response.status_code, status)
    #     self.assertEqual(response.data['Teste'], "teste")

    # def test_error_all_tutoring(self, **kwargs):
    #     api_url = '/all_tutoring/'
    #     status = HTTP_500_INTERNAL_SERVER_ERROR
    #     data = {'error': 'Error no servidor'}

    #     response = self.client.get(api_url)

    #     self.assertEqual(response.status_code, status)
    #     self.assertEqual(response.data, data)



