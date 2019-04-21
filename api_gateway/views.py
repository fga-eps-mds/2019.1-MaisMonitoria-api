from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
import requests
import json
import os


import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

# Initialize the default app
#cred = credentials.Certificate('serviceAccountKey.json')
#default_app = firebase_admin.initialize_app(cred)


@api_view(["GET"])
def all_tutoring(request):
    ## Verificação do token
    #decoded_token = auth.verify_id_token(request.data['access_token'])
    #uid_json = {"id": decoded_token['uid'], "name": decoded_token['name']}
    
    #id = json.dumps(uid_json)
    try:
        response = requests.get('http://api-monitoria:8001' + '/tutoring/')
        try:
            respose_json = response.json()
            return Response(data=respose_json, status=HTTP_200_OK)
        except:
            Response(response)
    except:
        return Response({'error': 'Error no servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

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
def delete_tutoring(request):
    ## Verificação do token
    #decoded_token = auth.verify_id_token(request.data['access_token'])
    #uid_json = {"id": decoded_token['uid'], "name": decoded_token['name']}
    
    #id = json.dumps(uid_json)
    try:
        response = requests.delete('http://api-monitoria:8001' + '/tutoring/'+ 
                                    str(request.data.get("id_tutoring_session"))+'/')
        return Response({"Success":"Excluido com sucesso"}, status=HTTP_200_OK)
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
