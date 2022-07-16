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
        fields = ['id','name','books']
        depth =1

class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    genre = GenresSerializer()
    class Meta:
        model = Book
        fields = ['id','name','description','genre','author','uploaded_at','image','file','filesize','audio','downloaded','shared','viewed','comments']
       