from rest_framework import serializers
from .models import Kitobxon
class KitobxonSerializer(serializers.ModelSerializer):
        class Meta:
            model = Kitobxon
            fields = ['url','name','user','starred']