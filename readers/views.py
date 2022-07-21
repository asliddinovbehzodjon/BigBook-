from time import time
from django.shortcuts import render
from rest_framework.response import Response
from datetime import date, datetime,timedelta
from rest_framework.views import APIView
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
    pagination_class = None
class TimeInfo(APIView):
    def get(self):
        today = datetime.today()
        oneweek = today - timedelta(days=7)
        oneday = today - timedelta(days=1)
        onemonth = today - timedelta(days=30)
        oneweekfilter = BotUsers.objects.filter(added__gte=oneweek,added__lte=today)
        serializer = BotUserSerializer(oneweek,many=True)
        return Response(serializer.data)
    
        
        
