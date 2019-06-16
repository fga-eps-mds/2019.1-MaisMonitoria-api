from rest_framework.test import APITestCase
from rest_framework import status
from api.utils import get_request


class ApiUserRedirectTests(APITestCase):
    def setUp(self):
        self.response_data = '{"error": "Error no servidor"}'
        self.invalid_url = ''
        self.invalid_route = ''
        self.invalid_param = ''

    def test_error_get_request(self):
        data = self.response_data
        request_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = get_request(self.invalid_url, self.invalid_route, self.invalid_param)
        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, request_status)
