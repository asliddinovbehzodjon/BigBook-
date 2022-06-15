from django.shortcuts import render

# Create your views here.
from .models import Kitobxon
from .serializer import KitobxonSerializer
from rest_framework.viewsets import ModelViewSet
class AllReaders(ModelViewSet):
    queryset = Kitobxon.objects.all()
    serializer_class = KitobxonSerializer