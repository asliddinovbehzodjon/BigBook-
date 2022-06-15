from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status
# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import GenresSerializer,BookSerializer
class AllGenres(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
class AllBooks(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    @action(methods=['post', 'get'], detail=True)
    def viewed(self, request, pk=None):
        kitob = get_object_or_404(Book, pk=pk)
        kitob.viewed = kitob.viewed + 1
        kitob.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post', 'get'], detail=True)
    def shared(self, request, pk=None):
        kitob = get_object_or_404(Book, pk=pk)
        kitob.shared = kitob.shared + 1
        kitob.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post', 'get'], detail=True)
    def downloaded(self, request, pk=None):
        kitob = get_object_or_404(Book, pk=pk)
        kitob.downloaded = kitob.downloaded + 1
        kitob.save()
        return Response(status=status.HTTP_200_OK)