from django.contrib import admin

# Register your models here.
from .models import Kitobxon,BotUsers
@admin.register(Kitobxon)
class Kitobxon(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name','user.username']
    search_help_text = "Kitobxon qidirish uchun kalit so'z kiriting"
    list_per_page = 10
    list_max_show_all = 15
@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ['name','username','telegram_id','added']
    search_fields = ['name','telegram_id','username']
    search_help_text = "User qidirish uchun kalit so'z kiriting"
    list_per_page = 10
    list_max_show_all = 15
    list_select_related = ['name','telegram_id']
    list_filter = ['added']
    list_display_links = ['telegram_id']
    list_editable = ['name','username']
    
    