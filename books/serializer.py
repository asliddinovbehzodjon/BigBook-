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
        depth=2
class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id','name','books']
        depth =1

class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    genres = GenresSerializer(read_only=True,many=True)
    class Meta:
        model = Book
        fields = ['id','name','description','genres','author','uploaded_at','image','file','filesize','audio','downloaded','shared','viewed','comments']
        depth=1