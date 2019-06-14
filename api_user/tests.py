from rest_framework.test import APITestCase
from rest_framework import status
import requests_mock
import json
import mock


class ApiUserRedirectTests(APITestCase):
    def setUp(self):
        self.id = {
            'id': '1',
        }

        self.valid_payload = {
            'access_token': '123'
        }

        self.invalid_payload = {
            'access_token': ''
        }

        self.valid_payload_teste = {
            'access_token': '123',
            'monitor_id': '1',
        }

        self.invalid_payload_teste = {
            'access_token': '',
            'monitor_id': '',
        }
        self.valid_payload_update = {
            'access_token': '123',
            'photo': 'null'
        }
        self.valid_payload_create = {
            'access_token': '123',
            'photo': 'null',
            'user_account_id': '4',
            'email': 'test@test.com'
        }

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1', 'id': '1'}))
    @requests_mock.Mocker(kw='mock')
    def test_get_monitor(self, **kwargs):
        request_id = self.valid_payload_teste
        api_url = '/get_monitor/'
        request_url = 'http://api-monitoria:8001/user/1'
        request_status = status.HTTP_200_OK
        data = {"Teste": "teste"}

        kwargs['mock'].get(request_url, text=json.dumps(data))

        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['Teste'], "teste")

    def test_error_get_monitor(self, **kwargs):
        request_id = self.invalid_payload_teste
        api_url = '/get_monitor/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)

    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1', 'id': '1'}))
    @requests_mock.Mocker(kw='mock')
    def test_get_user(self, **kwargs):
        request_id = self.valid_payload
        api_url = '/get_user/'
        request_url = 'http://api-monitoria:8001/user/1'
        request_status = status.HTTP_200_OK
        data = {"Teste": "teste"}

        kwargs['mock'].get(request_url, text=json.dumps(data))

        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data['Teste'], "teste")

    def test_error_get_user(self, **kwargs):
        request_id = self.invalid_payload
        api_url = '/get_user/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)

    @mock.patch('requests.put',
                mock.Mock(return_value={'status_code': 'HTTP_200_OK'}))
    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1', 'id': '1'}))
    @requests_mock.Mocker(kw='mock')
    def test_update_user(self, **kwargs):
        request_id = self.valid_payload_update
        api_url = '/update_user/'
        request_status = status.HTTP_200_OK

        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)

    def test_error_update_user(self, **kwargs):
        request_id = self.valid_payload_update
        api_url = '/update_user/'
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = '{"error": "Falha de autentica\\u00e7\\u00e3o"}'
        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)
        self.assertEqual(response.data, data)

    @mock.patch('requests.post',
                mock.Mock(return_value={'status_code': 'HTTP_201_CREATED'}))
    @mock.patch('firebase_admin.auth.verify_id_token',
                mock.Mock(return_value={'uid': '1', 'is_auth': True, 'email': 'teste'}))
    @requests_mock.Mocker(kw='mock')
    def test_create_user(self, **kwargs):
        request_id = self.valid_payload_create
        api_url = "http://localhost:8000/create_user/"
        request_status = status.HTTP_201_CREATED
        response = self.client.post(api_url, request_id)
        self.assertEqual(response.status_code, request_status)
