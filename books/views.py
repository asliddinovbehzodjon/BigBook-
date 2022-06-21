from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.
from django.db.models import  Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import GenresSerializer,BookSerializer,CommentSerializer
class AllGenres(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
class AllBooks(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    @action(methods=['post', 'get'], detail=True)
    def view(self, request, pk=None):
        kitob = get_object_or_404(Book, pk=pk)
        kitob.viewed = kitob.viewed + 1
        kitob.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post', 'get'], detail=True)
    def share(self, request, pk=None):
        kitob = get_object_or_404(Book, pk=pk)
        kitob.shared = kitob.shared + 1
        kitob.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post', 'get'], detail=True)
    def download(self, request, pk=None):
        kitob = get_object_or_404(Book, pk=pk)
        kitob.downloaded = kitob.downloaded + 1
        kitob.save()
        return Response(status=status.HTTP_200_OK)
class CommentWrite(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
class MoreViewed(APIView):
    def get(self,request):
        kitoblar = Book.objects.all().order_by('-viewed')[:3]
        serializer = BookSerializer(kitoblar,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
class SearchBook(APIView):
    pagination_class = LimitOffsetPagination
    def get(self,request,key):
         kitoblar=Book.objects.filter(Q(name__icontains=key) | Q(description__icontains=key) | Q(author__icontains=key))
         serializer = BookSerializer(kitoblar,many=True,context={'request':request})
         return Response(serializer.data,status=status.HTTP_302_FOUND)