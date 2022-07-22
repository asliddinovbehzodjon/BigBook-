from django.shortcuts import render
from rest_framework.response import Response
from datetime import datetime,timedelta,date
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
    def get(self,request):
        today = date.today()
        nextday = today+ timedelta(days=1)
        oneweek = today - timedelta(days=7)
        oneday = today + timedelta(days=1)
        onemonth = today - timedelta(days=30)
        onedayfilter = BotUsers.objects.filter(added__range=[today,oneday]).count()
        oneweekfilter = BotUsers.objects.filter(added__range=[oneweek,nextday]).count()
        onemonthfilter = BotUsers.objects.filter(added__range=[onemonth,nextday]).count()
        allfilter = BotUsers.objects.all().count()
        return Response(data= {'today':onedayfilter,'lastweek':oneweekfilter,'lastmonth':onemonthfilter,'all':allfilter})
    
class AllBotUsers(ModelViewSet):
    queryset = BotUsers.objects.all().only('telegram_id')
    serializer_class = BotUserSerializer
    pagination_class = None
            
        
