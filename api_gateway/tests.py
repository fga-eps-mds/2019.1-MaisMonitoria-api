from rest_framework.test import APITestCase
from rest_framework import status
import requests_mock
import json
import mock


class MonitoringRedirectTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'access_token': '123',
            'page': ''
        }

        self.valid_payload_2 = {
            'access_token': '123',
            'page': '2'
        }

        self.valid_payload_get_tutoring = {
            'access_token': '123',
            'id_tutoring_session': '3'
        }

        self.invalid_payload = {
            'name': ''
        }

        self.valid_payload_search = {
            'access_token': '123',
            'search': 'lola'
        }

        self.invalid_payload_search = {
            'access_token': '123',
            'search': 'asd'
        }

        self.valid_payload_like = {
            'access_token': '123',
            'tutoring_session': '10'
        }

        self.valid_payload_like_delete = {
            'access_token': '1010',
            'id_like': 2
        }
        self.valid_payload_create = {
            'access_token': 'asdsd',
            'name': 'teste',
            'subject': 'teste',
            'description': 'teste',
        }
        self.valid_payload_update_tutoring = {
            'access_token': '1010',
            'id_tutoring_session': 2,
            'monitor': "asd",
            'name': 'teste'
        }
        self.invalid_payload_update_tutoring = {
            'access_token': '',
            'id_tutoring_session': 2,
            'monitor': "asd",
            'name': 'teste'
        }
        self.valid_payload_tutoring_delete = {
            'access_token': '1010',
            'id_tutoring': 1
        }

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': 'yes'}))
    @requests_mock.Mocker(kw='mock')
    def test_search_tutoring(self, **kwargs):
        request_url = 'http://api-monitoria:8001/tutoring/?search=lola'
        search = self.valid_payload_search
        api_url = '/search_tutoring/'
        data = {"teste": "resposta"}
        request_status = status.HTTP_200_OK

        kwargs['mock'].get(request_url, text=json.dumps(data))
        response = self.client.post(api_url, search)

        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['teste'], "resposta")

    def test_error_search_tutoring(self, **kwargs):
        search = self.valid_payload_search
        api_url = '/search_tutoring/'
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        response = self.client.post(api_url, search)

        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': 'yes'}))
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

        response = self.client.post(api_url, self.valid_payload)

        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': 'yes'}))
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
        kwargs['mock'].get(request_url, text=json.dumps(data))
        response = self.client.post(api_url, param)

        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['name'], 'erererree')

    def teste_error_get_tutoring(self, **kwargs):
        id = self.valid_payload
        api_url = '/get_tutoring/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'

        response = self.client.post(api_url, id)

        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1'}))
    @requests_mock.Mocker(kw='mock')
    def test_like_tutoring(self, **kwargs):
        api_url = "http://localhost:8000/like_tutoring/"
        param = self.valid_payload_like
        request_url = 'http://api-monitoria:8001/like/'
        request_status = status.HTTP_201_CREATED
        data = {
            'user_that_likes': '1',
            'tutoring_session': '10'
        }

        kwargs['mock'].post(request_url, headers=data)
        response = self.client.post(api_url, param, format='json')

        self.assertEqual(response.status_code, request_status)

    def test_error_like_tutoring(self):
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        param = self.valid_payload_like
        api_url = "http://localhost:8000/like_tutoring/"

        response = self.client.post(api_url, param, format='json')

        self.assertEqual(response.data, data)

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': 'yes'}))
    @requests_mock.Mocker(kw='mock')
    def test_delete_like(self, **kwargs):
        api_url = 'http://localhost:8000/like_delete/'
        request_url = 'http://api-monitoria:8001/like/2'
        request_status = status.HTTP_200_OK

        kwargs['mock'].delete(request_url)
        response = self.client.post(api_url, self.valid_payload_like_delete, format='json')

        self.assertEqual(response.status_code, request_status)

    def test_error_delete_like(self, **kwargs):
        param = self.valid_payload_like_delete
        api_url = 'http://localhost:8000/like_delete/'
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        status_request = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = self.client.post(api_url, param, format='json')

        self.assertEqual(response.status_code, status_request)
        self.assertEqual(response.data, data)

    @mock.patch('requests.post',
                mock.Mock(return_value={'status_code': 'HTTP_201_CREATED'}))
    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1', 'is_auth': True}))
    @requests_mock.Mocker(kw='mock')
    def test_create_tutoring(self, **kwargs):
        api_url = "http://localhost:8000/create_tutoring/"
        param = self.valid_payload_create
        request_status = status.HTTP_201_CREATED
        response = self.client.post(api_url, param, format='json')
        self.assertEqual(response.status_code, request_status)

    @requests_mock.Mocker(kw='mock')
    def test_error_create_tutoring(self, **kwargs):
        api_url = "http://localhost:8000/create_tutoring/"
        param = self.valid_payload_create
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = self.client.post(api_url, param, format='json')
        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, request_status)

    @mock.patch('requests.put',
                mock.Mock(return_value={'status_code': 'HTTP_200_OK'}))
    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1', 'is_auth': True}))
    @requests_mock.Mocker(kw='mock')
    def test_update_tutoring(self, **kwargs):
        param = self.valid_payload_update_tutoring
        api_url = '/update_tutoring/'
        request_status = status.HTTP_200_OK
        response = self.client.post(api_url, param, format='json')
        self.assertEqual(response.status_code, request_status)

    def test_error_update_tutoring(self, **kwargs):
        param = self.invalid_payload_update_tutoring
        api_url = '/update_tutoring/'
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = self.client.post(api_url, param, format='json')
        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, request_status)

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': 'yes'}))
    @requests_mock.Mocker(kw='mock')
    def test_2_all_tutoring2(self, **kwargs):
        api_url = '/all_tutoring/'
        request_url = 'http://api-monitoria:8001/tutoring/'
        request_status = status.HTTP_200_OK
        data = {"Teste": "teste"}
        kwargs['mock'].get(request_url, text=json.dumps(data))
        response = self.client.post(api_url, self.valid_payload_2)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['Teste'], "teste")

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': 'yes'}))
    @requests_mock.Mocker(kw='mock')
    def test_delete_monitoring(self, **kwargs):
        api_url = 'http://localhost:8000/delete_tutoring/'
        request_url = 'http://api-monitoria:8001/tutoring/1'
        request_status = status.HTTP_200_OK

        kwargs['mock'].delete(request_url)
        response = self.client.post(api_url, self.valid_payload_tutoring_delete, format='json')

        self.assertEqual(response.status_code, request_status)
