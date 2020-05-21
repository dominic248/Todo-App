import jwt,json
from rest_framework import views,status, exceptions
from rest_framework.response import Response
from django.http import HttpResponse
from django.conf import settings
from rest_framework.authentication import get_authorization_header, BaseAuthentication

from django.contrib.auth import get_user_model
User=get_user_model() 

class Hello(views.APIView):
    def get(self,request): 
        return Response({"status":"good "+str(request.user.username)})
        