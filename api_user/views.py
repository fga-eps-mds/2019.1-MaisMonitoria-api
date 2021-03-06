from api.utils import verify_auth, get_request, put_request
from api.utils import post_request, registry_auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import os

URL = os.getenv('URL_SERVICE_MONITORIA')
ROUTE = 'user/'


@api_view(["POST"])
def get_user(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        param = auth_response['id']
        return get_request(URL, ROUTE, param)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def update_user(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        param = auth_response['id']
        data = request.data.copy()
        data['user_account_id'] = auth_response['id']
        del data['access_token']

        if data['photo'] != 'null':
            photo = {}
            photo['photo'] = (request.data['photo'].name, request.data['photo'].file.getvalue())
            del data['photo']

            return put_request(URL, ROUTE, param, data, photo)

        del data['photo']
        return put_request(URL, ROUTE, param, data)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def create_user(request):
    token = request.data['access_token']
    auth_response = registry_auth(token)

    if auth_response['is_auth']:
        data = request.data.copy()
        data['user_account_id'] = auth_response['id']
        data['email'] = auth_response['email']
        del data['access_token']

        if data['photo'] != 'null':
            photo = {}
            photo['photo'] = (request.data['photo'].name, request.data['photo'].file.getvalue())
            del data['photo']

            return post_request(URL, ROUTE, data, photo)

        del data['photo']
        return post_request(URL, ROUTE, data)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def get_monitor(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        param = str(request.data['monitor_id'])
        return get_request(URL, ROUTE, param)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
