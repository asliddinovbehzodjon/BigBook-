from rest_framework import serializers
from .models import Book,Comments,Genres
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        
class BookSerialzerforGenres(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name','description','author','uploader','uploaded_at','image','file','filesize','audio','downloaded','shared','viewed']
class GenresSerializer(serializers.HyperlinkedModelSerializer):
    # books = BookSerialzerforGenres(read_only=True,many=True)
    class Meta:
        model = Genres
        fields = ['url','id','name','books']
class BookSerializer(serializers.HyperlinkedModelSerializer):
    # uploader = serializers.StringRelatedField()
    comments = CommentSerializer(read_only=True,many=True)


    class Meta:
        model = Book
        fields = ['url','name','description','genre','author','uploader','uploaded_at','image','file','filesize','audio','downloaded','shared','viewed','comments']
