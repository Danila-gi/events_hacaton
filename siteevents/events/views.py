from click import password_option
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from events.models import User
from django.core.exceptions import ObjectDoesNotExist
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView):
    def post(self, request):
        try:
            user_login = User.objects.get(login=request.data['username'])
            try:
                user = User.objects.get(login=request.data['username'], password=request.data['password'])
                return Response({'id': user.id, 'user': user.login, 'flag': True})
            except ObjectDoesNotExist:
                return Response({'id': user_login.id, 'user': user_login.login, 'flag': False})
        except ObjectDoesNotExist:
            return Response({'id': '', 'user': '', 'flag': False})

class RegistrationAPIView(APIView):
    def post(self, request):
        try:
            User.objects.get(login=request.data['username'])
            return Response({'id': None, 'user': None})
        except:
            try:
                login = request.data['username']
                pswd = request.data['password']
                user = User(login=login, password=pswd)
                user.save()

                user = User.objects.get(login=request.data['username'])
                return Response({'id': user.id, 'user': user.login})
            except:
                return Response({'id': None, 'user': None})

class TagsGetAPIView(APIView):
    def post(self, request):
        tags = request.data['tags']
        user = User.objects.get(id=request.data['id'])
        user.tags = '/'.join(tags)
        user.save()

class TagsSendAPIView(APIView):
    def post(self, request):
        user = User.objects.get(id=request.data['id'])
        return Response({'tags': user.tags.split('/')})

class FavouritesGetAPIView(APIView):
    def post(self, request):
        event = request.data['event']
        user = User.objects.get(id=request.data['id'])
        user.favourites = user.favourites + '/' + str(event)
        user.save()

class FavouritesSendAPIView(APIView):
    def post(self, request):
        user = User.objects.get(id=request.data['id'])
        return Response({'events': user.favourites.split('/')})