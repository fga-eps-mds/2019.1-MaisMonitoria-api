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

import ast
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

x = os.getenv('FIREBASE_KEY')
x = ast.literal_eval(x)
cred = credentials.Certificate(x)
default_app = firebase_admin.initialize_app(cred)

@api_view(["POST"])
def get_user(request):
    ## Verificação do token
    decoded_token = auth.verify_id_token(request.data['access_token'])
    uid_json = {"id": decoded_token['uid']}

    try:
        response = requests.get('http://api-monitoria:8001' + '/user/'+ 
                                    str(request.data.get("user_account_id"))+'/')
        try:
            respose_json = response.json()
            return Response(data=respose_json, status=HTTP_200_OK)
        except:
            Response(response)
    except:
        return Response({'error': 'Error no servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def update_user(request):
    ## Verificação do token
    #decoded_token = auth.verify_id_token(request.data['access_token'])
    #uid_json = {"id": decoded_token['uid'], "name": decoded_token['name']}
    
    #id = json.dumps(uid_json)
    try:
        response = requests.put('http://api-monitoria:8001' + '/user/'+
                            str(request.data.get("user_account_id"))+'/', data=request.data)

        return Response({"Success":"Alterado com sucesso"}, status=HTTP_200_OK)
    except:
        return Response({'error': 'Error no servidor'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
