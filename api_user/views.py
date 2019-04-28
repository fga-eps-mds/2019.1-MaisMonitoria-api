from api.utils import verify_auth, get_request, put_request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status

import requests
import json
import os

URL = 'http://api-monitoria:8001/'
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

    if auth_response["is_auth"]:
        param = auth_response['id']
        data = request.data
        del data['access_token']
        return put_request(URL, ROUTE, param, data)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
