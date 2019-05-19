from firebase_admin import auth, credentials, initialize_app
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import ast
import os

FIREBASE_KEY = os.getenv('FIREBASE_KEY')
FIREBASE_KEY = ast.literal_eval(FIREBASE_KEY)
CRED = credentials.Certificate(FIREBASE_KEY)
DEFAULT_APP = initialize_app(CRED)

def verify_auth(token):
    try:
        decoded_token = auth.verify_id_token(token)
        response = {
            'is_auth': True, 
            'id': decoded_token['uid']
        } 
        return response
    except:
        response = {'is_auth': False}
        return response
    

def registry_auth(token):
    try:
        decoded_token = auth.verify_id_token(token)
        response = {
            'is_auth': True,
            'id': decoded_token['uid'],
            'email': decoded_token['email']
        } 
        return response
    except:
        response = {'is_auth': False}
        return response

def get_request(url, route, param=None):
    try:
        if param is not None:
            request_url = url + route + param + '/'
        else:
            request_url = url + route
        response = requests.get(request_url)
        respose_json = response.json()
        return Response(data=respose_json, status=status.HTTP_200_OK)
    except:
        respose_json = {
            'error': 'Error no servidor'
        }
        return Response(data=json.dumps(respose_json), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def put_request(url, route, param, data, photo=None):
    try:
        if photo:
            requests.put(url + route + param + '/', data=data, files=photo)
        else:
            requests.put(url + route + param + '/', data=data)

        response_json = {
            "success":"Alterado com sucesso"
        }
        return Response(data=json.dumps(response_json), 
                        status=status.HTTP_200_OK)
    except:
        respose_json = {
            'error': 'Error no servidor'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def post_request(url, route, data, photo=None):
    try:
        if photo:
            requests.post(url + route, data=data, files=photo)
        else:
            requests.post(url + route, data=data)
            
        response_json = {
            "success":"Cadastrado com sucesso"
        }
        return Response(data=json.dumps(response_json), 
                        status=status.HTTP_201_CREATED)
    except:
        respose_json = {
            'error': 'Error no servidor'
        }
        return Response(data=json.dumps(respose_json), 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)