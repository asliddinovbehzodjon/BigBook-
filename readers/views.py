from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from .models import Kitobxon,BotUsers
from .serializer import KitobxonSerializer,BotUserSerializer
from rest_framework.viewsets import ModelViewSet
class AllReaders(ModelViewSet):
    queryset = Kitobxon.objects.all()
    serializer_class = KitobxonSerializer
class BotUsersAll(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class  = BotUserSerializer
    
