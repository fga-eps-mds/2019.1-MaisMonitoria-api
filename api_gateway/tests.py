from api_gateway.views import all_tutoring
import requests_mock
from rest_framework.test import APITestCase
import json
import unittest

from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)

class MonitoringRedirectTests(APITestCase, unittest.TestCase):
    def setUp(self):
        self.valid_payload = {
            'id_tutoring_session': '1'
        }

        self.invalid_payload = {
            'name': ''
        }


        self.valid_payload_search={
            'access_token': "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyZjBiNDZjYjc1OTBjNzRmNTNhYzdhOWUwY2IxYzAzMjRlY2RkNzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbWFpc21vbml0b3JpYS1mZTMxYyIsImF1ZCI6Im1haXNtb25pdG9yaWEtZmUzMWMiLCJhdXRoX3RpbWUiOjE1NTgyOTc4NzYsInVzZXJfaWQiOiI2RFFzY1pkdnZrZmdVbkNXajRhbGVFQm1qaEUzIiwic3ViIjoiNkRRc2NaZHZ2a2ZnVW5DV2o0YWxlRUJtamhFMyIsImlhdCI6MTU1ODMwMTk5MCwiZXhwIjoxNTU4MzA1NTkwLCJlbWFpbCI6IjEyMzRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIjEyMzRAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.rFLldBTlgtsdZ1SCseFGDSdmshNP7dCFxr8vlRRcbhfLTYm8iEHTIjqW3yRnxe_SUB-nzFegJ6_YBAAoTRwsvqT6YQP3vgnDa4GSGi8LfgnAzUnCNUOu84QzM4T6WSxFgjOu-5h2VnZgFhFgq2u2F5ql6PfJOyA5G2hnr2rosqcX_hB2e7tQbzHortQtaHuat-K-rZQGTNaa9-4EpKRlSVw1EhAeThEDierleUhhp9KP5iHNcPvc5Xa-KE6os3XMyspuYftljRcUc9ZgaP--ExY-H0BBchMYCaxBYlIj_ZISI2A-Ijo_SyUB74tX5o18xaPeYUYx5kpK22HhwM9LLQ",
            'search': ""
        }
        self.invalid_payload_search ={
            'access_token': '123',
            'search':'asd'
        }






#     @requests_mock.Mocker(kw='mock')
#     def test_all_tutoring(self, **kwargs):
#         api_url = '/all_tutoring/'
#         request_url = 'http://api-monitoria:8001/tutoring/'
#         status = HTTP_200_OK
#         data = {"Teste": "teste"}

#         kwargs['mock'].get(request_url, text=json.dumps(data))

#         response = self.client.get(api_url)

#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data['Teste'], "teste")

#     def test_error_all_tutoring(self, **kwargs):
#         api_url = '/all_tutoring/'
#         status = HTTP_500_INTERNAL_SERVER_ERROR
#         data = {'error': 'Error no servidor'}

#         response = self.client.get(api_url)

#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)

#     @requests_mock.Mocker(kw='mock')
#     def test_get_tutoring(self, **kwargs):
#         id = self.valid_payload
#         api_url = '/get_tutoring/'
#         request_url = 'http://api-monitoria:8001/tutoring/1/'

#         status = HTTP_200_OK
#         data = {'Teste': 'teste'}
#         kwargs['mock'].get(request_url,text = json.dumps(data))

#         response = self.client.post(api_url,id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data['Teste'] ,'teste'  )

#     def teste_error_get_tutoring(self, **kwargs):
#         id = self.valid_payload
#         api_url = '/get_tutoring/'

#         status = HTTP_500_INTERNAL_SERVER_ERROR
#         data = {'error': 'Error no servidor'} 
#         response = self.client.post(api_url,id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data ,data  )
        
#     @requests_mock.Mocker(kw= 'mock')    
#     def teste_delete_tutoring(self, **kwargs):
#         id= self.valid_payload
#         api_url = '/delete_tutoring/'
#         request_url = 'http://api-monitoria:8001/tutoring/1/'
#         data = {"Success":"Excluido com sucesso"}
#         status = HTTP_200_OK
        
#         kwargs['mock'].delete(request_url, text= json.dumps(data))
#         response = self.client.post(api_url, id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)

#     def teste_error_delete_tutoring(self, **kwargs):
#         id= self.valid_payload
#         api_url = '/delete_tutoring/'
#         data = {'error': 'Error no servidor'}
#         status =HTTP_500_INTERNAL_SERVER_ERROR
#         response = self.client.post(api_url, id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)
    
    
#     @requests_mock.Mocker(kw= 'mock')    
#     def teste_create_tutoring(self, **kwargs):
        
#         id= self.valid_payload
#         api_url = '/create_tutoring/'
#         request_url = 'http://api-monitoria:8001/tutoring/'
#         data = {"Success":"Criado com sucesso"}
#         status = HTTP_200_OK

#         kwargs['mock'].post(request_url, text= json.dumps(data))
#         response = self.client.post(api_url, id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)

#     def teste_error_create_tutoring(self, **kwargs):
#         id= self.valid_payload
#         api_url = '/create_tutoring/'
#         data = {'error': 'Error no servidor'}
#         status =HTTP_500_INTERNAL_SERVER_ERROR
#         response = self.client.post(api_url, id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)  

#     @requests_mock.Mocker(kw= 'mock')    
#     def teste_update_tutoring(self, **kwargs):
#         id= self.valid_payload
#         api_url = '/update_tutoring/'
#         request_url = 'http://api-monitoria:8001/tutoring/1/'
#         data = {"Success":"Alterado com sucesso"}
#         status = HTTP_200_OK
        
#         kwargs['mock'].put(request_url, text= json.dumps(data))
#         response = self.client.post(api_url, id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)

#     def teste_error_update_tutoring(self, **kwargs):
#         id= self.valid_payload
#         api_url = '/delete_tutoring/'
#         data = {'error': 'Error no servidor'}
#         status =HTTP_500_INTERNAL_SERVER_ERROR
#         response = self.client.post(api_url, id)
#         self.assertEqual(response.status_code, status)
#         self.assertEqual(response.data, data)

    @requests_mock.Mocker(kw='mock')
    def test_search_tutoring(self, **kwargs):
        search = self.valid_payload_search
        api_url = '/search_tutoring/'
        request_url= 'http://api-monitoria:8001/tutoring/?search='
        status = HTTP_200_OK
        data = {"teste":"resposta"}
        kwargs['mock'].get(request_url, text= json.dumps(data))
        response = self.client.post(api_url,search)
        self.assertEqual(response.status_code, status)
        self.assertEqual(response.data['teste'], "resposta")



