from rest_framework import serializers
from .models import Kitobxon,BotUsers
class KitobxonSerializer(serializers.ModelSerializer):
        class Meta:
            model = Kitobxon
            fields = ['url','name','user','starred']
class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        read_onyl_fields = ['added']
        fields = ['id','name','telegram_id','username','added']