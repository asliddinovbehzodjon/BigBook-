from django.contrib import admin

# Register your models here.
from .models import Kitobxon
@admin.register(Kitobxon)
class Kitobxon(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name','user.username']
    search_help_text = "Kitobxon qidirish uchun kalit so'z kiriting"
    list_per_page = 10
    list_max_show_all = 15