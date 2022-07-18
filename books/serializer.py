from rest_framework import serializers
from .models import Book,Comments,Genres
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        
class BookSerialzerforGenres(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name','genre','description','author','uploaded_at','image','file','filesize','audio','downloaded','shared','viewed']
    
class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id','name','genres']
        depth =2

class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    
    class Meta:
        model = Book
        fields = ['url','id','name','description','genre','author','uploaded_at','image','file','filesize','audio','downloaded','shared','viewed','comments']
       