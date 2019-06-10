from api.utils import verify_auth, get_request, put_request, post_request, delete_request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status

import requests
import json
import os

URL = 'http://api-monitoria:8001/'
ROUTE = 'tutoring/'

@api_view(["POST"])
def all_tutoring(request):
    token = request.data['access_token']
    page = request.data['page']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        if page:
            route = ROUTE+'?page='+str(page)
            return get_request(URL, route)
        return get_request(URL, ROUTE)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def search_tutoring(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        param = str(request.data['search'])
        param = '?search=' + param
        return get_request(URL, ROUTE, param)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def get_tutoring(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        param = str(request.data['id_tutoring_session'])
        return get_request(URL, ROUTE, param)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_tutoring(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        data = request.data
        data['monitor'] = auth_response['id']
        del data['access_token']
        return post_request(URL, ROUTE, data)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def update_tutoring(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response["is_auth"]:
        param = str(request.data['id_tutoring_session'])
        data = request.data
        data['monitor'] = auth_response['id']
        del data['access_token']
        return put_request(URL, ROUTE, param, data)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def like_tutoring(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response["is_auth"]:
        route = 'like/'
        data = request.data
        data['user_that_likes']= auth_response['id']
        del data['access_token']
        return post_request(URL, route, data)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def delete_like(request):
    token = request.data['access_token']
    auth_response = verify_auth(token)

    if auth_response["is_auth"]:
        route = 'like/'
        param = str(request.data['id_like'])
        return delete_request(URL,route,param)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


