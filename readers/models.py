from tabnanny import verbose
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Kitobxon(models.Model):
    name = models.CharField(max_length=5000,verbose_name="Kitobxon nomi",help_text="Kitobxon nomini kiriting",default="Kitobxon")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    starred = models.PositiveIntegerField(default=0,verbose_name="kitobxon statusi",help_text="Kitobxon statusini kiriting")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Kitobxonlar"
        verbose_name = "Kitobxon "
        verbose_name_plural = "Kitobxonlar "
class BotUsers(models.Model):
    name = models.CharField(max_length=1000,null=True,blank=True,help_text="User ismi",verbose_name="User ismi")
    telegram_id = models.IntegerField(verbose_name="Telegram ID",help_text="User Telegram Id si",unique=True)
    added = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=1000,null=True,blank=True,help_text="UUser username i",verbose_name="User username i")
    class Meta:
        verbose_name = "Bot User"
        verbose_name_plural = "Bot Users"
        db_table = "Bot Users"