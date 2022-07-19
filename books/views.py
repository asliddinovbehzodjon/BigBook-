from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
# Create your views here.
from .pagination import PaginationHandlerMixin
from django.db.models import  Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import GenresSerializer,BookSerializer,CommentSerializer
class BasicPagination(PageNumberPagination):
   def get_paginated_response(self, data):
        return Response({
        
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page_num':self.page.number,
            'all_pages':self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            
            'results': data
        })
class AllGenres(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    pagination_class = BasicPagination
class AllBooks(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BasicPagination

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
class MoreDownloaded(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination
    
    def get(self,request):
        kitoblar = Book.objects.all().order_by('-downloaded')
        page = self.paginate_queryset(kitoblar)
        if page is not None:
            serializer = self.get_paginated_response(BookSerializer(page,
                many=True).data)
        else:
            serializer = BookSerializer(kitoblar, many=True)
      
        return Response(serializer.data,status=status.HTTP_200_OK)
class SearchBook(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination
    def get(self,request,key):
        kitoblar=Book.objects.filter(Q(name__icontains=key) | Q(description__icontains=key) | Q(author__icontains=key))
        page = self.paginate_queryset(kitoblar)
        if page is not None:
            serializer = self.get_paginated_response(BookSerializer(page,
                many=True).data)
        else:
            serializer = BookSerializer(kitoblar, many=True)
      
        return Response(serializer.data,status=status.HTTP_200_OK)
class MoreGenre(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination
    def get(self,request,genre,id):
        kitoblar=Book.objects.filter(genre=genre).exclude(id=id).order_by('-downloaded')
        page = self.paginate_queryset(kitoblar)
        if page is not None:
            serializer = self.get_paginated_response(BookSerializer(page,
                many=True).data)
        else:
            serializer = BookSerializer(kitoblar, many=True)
      
        return Response(serializer.data,status=status.HTTP_200_OK)
          