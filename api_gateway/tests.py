from rest_framework.test import APITestCase
from api_gateway.views import all_tutoring
from rest_framework import status 
import firebase_admin
import requests_mock
import json
import mock

class MonitoringRedirectTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'access_token': '123',            
        }
        self.valid_payload_get_tutoring = {
             'access_token': '123',
             'id_tutoring_session': '3'
        }

        self.invalid_payload = {
            'name': ''
        }

        self.valid_payload_search={
            'access_token': '123',
            'search': 'lola'
        }

        self.invalid_payload_search ={
            'access_token': '123',
            'search':'asd'
        }
        self.valid_payload_like = {
            'access_token': '123',
            'tutoring_session':'10'

        }

    @mock.patch('firebase_admin.auth.verify_id_token', mock.Mock(return_value={ 'uid': 'yes' }))
    @requests_mock.Mocker(kw='mock')
    def test_search_tutoring(self, **kwargs):
        request_url = 'http://api-monitoria:8001/tutoring/?search=lola'
        search = self.valid_payload_search
        api_url = '/search_tutoring/'
        data = {"teste":"resposta"}
        request_status = status.HTTP_200_OK

        kwargs['mock'].get(request_url, text= json.dumps(data))
        response = self.client.post(api_url, search)
        
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['teste'], "resposta")

    @mock.patch('firebase_admin.auth.verify_id_token', mock.Mock(return_value={ 'uid': 'yes' }))
    @requests_mock.Mocker(kw='mock')
    def test_all_tutoring(self, **kwargs):
        api_url = '/all_tutoring/'
        request_url = 'http://api-monitoria:8001/tutoring/'
        request_status = status.HTTP_200_OK
        data = {"Teste": "teste"}

        kwargs['mock'].get(request_url, text=json.dumps(data))

        response = self.client.post(api_url, self.valid_payload)

        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['Teste'], "teste")

    def test_error_all_tutoring(self, **kwargs):
        api_url = '/all_tutoring/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'

        response = self.client.post(api_url,self.valid_payload)
        
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)


    @mock.patch('firebase_admin.auth.verify_id_token', mock.Mock(return_value={ 'uid': 'yes' }))
    @requests_mock.Mocker(kw='mock')
    def test_get_tutoring(self, **kwargs):
        param = self.valid_payload_get_tutoring
        api_url = '/get_tutoring/'
        request_url = 'http://api-monitoria:8001/tutoring/3'

        request_status = status.HTTP_200_OK
        data = {
                    "monitor": "deSLYBKUgfa21j1cuOq1XGKLGR23",
                    "id_tutoring_session": 3,
                    "name": "erererree",
                    "subject": "rerererew",
                    "applicants": [],
                    "description": "werwrerwrew",
                    "status_tutoring_session": False,
                    "create_date": "2019-05-12T23:12:35.180873Z",
                    "accepted_applicants": []
                }
        kwargs['mock'].get(request_url,text = json.dumps(data))

        response = self.client.post(api_url,param)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['name'] ,'erererree' )


    def teste_error_get_tutoring(self, **kwargs):
        id = self.valid_payload
        api_url = '/get_tutoring/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        
        response = self.client.post(api_url, id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)
        
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

    @mock.patch('firebase_admin.auth.verify_id_token', mock.Mock(return_value={'uid':'1'}))
    @requests_mock.Mocker(kw='mock')
    def test_like_tutoring(self, **kwargs):
        api_url = "http://localhost:8000/like_tutoring/"
        param =  self.valid_payload_like
        request_url = 'http://api-monitoria:8001/like/'
        request_status = status.HTTP_201_CREATED
        data= {'user_that_likes': '1',
                'tutoring_session':'10'}
               

        kwargs['mock'].post(request_url,headers=data)
        response = self.client.post(api_url,param, format='json')
        self.assertEqual(response.status_code, request_status)
        

       



