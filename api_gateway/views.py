from api.utils import verify_auth, get_request, put_request, post_request
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
    auth_response = verify_auth(token)

    if auth_response['is_auth']:
        return get_request(URL, ROUTE)
    else:
        respose_json = {
            'error': 'Falha de autenticação'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def get_tutoring(request):
    ## Verificação do token
    #decoded_token = auth.verify_id_token(request.data['access_token'])
    #uid_json = {"id": decoded_token['uid'], "name": decoded_token['name']}
    
    #id = json.dumps(uid_json)
    try:
        response = requests.get('http://api-monitoria:8001' + '/tutoring/'+ 
                                    str(request.data.get("id_tutoring_session"))+'/')
        try:
            respose_json = response.json()
            return Response(data=respose_json, status=HTTP_200_OK)
        except:
            Response(response)
    except:
        return Response({'error': 'Error no servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_tutoring(request):
    ## Verificação do token
    #decoded_token = auth.verify_id_token(request.data['access_token'])
    #uid_json = {"id": decoded_token['uid'], "name": decoded_token['name']}
    
    #id = json.dumps(uid_json)
    try:
        response = requests.post('http://api-monitoria:8001' + '/tutoring/', data=request.data)
        try:
            respose_json = response.json()
            return Response(data=respose_json, status=HTTP_200_OK)
        except:
            Response(response)
    except:
        return Response({'error': 'Error no servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def update_tutoring(request):
    ## Verificação do token
    #decoded_token = auth.verify_id_token(request.data['access_token'])
    #uid_json = {"id": decoded_token['uid'], "name": decoded_token['name']}
    
    #id = json.dumps(uid_json)
    try:
        response = requests.put('http://api-monitoria:8001' + '/tutoring/'+
                            str(request.data.get("id_tutoring_session"))+'/', data=request.data)

        return Response({"Success":"Alterado com sucesso"}, status=HTTP_200_OK)
    except:
        return Response({'error': 'Error no servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
