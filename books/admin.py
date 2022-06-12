from django.contrib import admin

# Register your models here.
from .models import Genres,Book,Comments
@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ['name']
    list_per_page = 10
    list_max_show_all = 15
    search_fields = ['name']
    search_help_text = "Janr qidirish uchun kalit so'z kiriting"
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','author','uploader','downloaded']
    list_max_show_all = 15
    list_per_page = 10
    list_filter = ['author','uploaded_at','genre']
    list_editable = ['author']
    list_display_links = ['name']
    search_fields = ['name','genre','descrition','author','uploader']
    search_help_text = "Kitob qidirish uchun kalit so'z kiriting..."
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment','book','writed']
    list_filter = ['book','writed']
    list_per_page = 10
    list_max_show_all = 15
    search_fields = ['comment','book']
    search_help_text = "Izoh qidirish uchun kalit so'z kiriting"