from django.db import models
from readers.models import Kitobxon
# Create your models here.
# Janrlar jadvali
class Genres(models.Model):
    name = models.CharField(max_length=500,verbose_name="Janr nomi",help_text="Janr nomi kiriting")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Janrlar"
        verbose_name = "Janr "
        verbose_name_plural = "Janrlar "
class Book(models.Model):
    name = models.CharField(max_length=5000,verbose_name="Kitob nomini",help_text="Kitob nomi kiriting")
    genre = models.ManyToManyField(Genres,verbose_name="Kitob janr(lar)i",help_text="Kitob janr(lar)i ni kiriting",related_name='janr')
    description = models.TextField(help_text="Kitob haqida qisqacha kiriting",verbose_name="Kitob haqida qisqacha")
    author = models.CharField(max_length=500,verbose_name="kitob muallifi",help_text="Kitob muallifini kiriting")
    uploader = models.ForeignKey(Kitobxon,on_delete=models.PROTECT,verbose_name="Kitob yuklagan shaxs",help_text="Kitob yuklagan shaxsni kiriting")
    image = models.ImageField(upload_to="book-images",null=True,blank=True,verbose_name="Kitob rasmi",help_text="Kitob rasmini kiriting")
    file = models.FileField(upload_to='book-files',verbose_name="Kitob fayli",help_text="Kitob faylini kiriting")
    audio = models.FileField(upload_to='book-audios',verbose_name="Kitob audio fayli",help_text="Kitob audio fayli",null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True,help_text="Kitob yuklangan vaqt",verbose_name="Kitob yuklangan vaqt")
    downloaded = models.PositiveIntegerField(default=1,verbose_name="Yuklanganlar soni",help_text='Yuklanganlar soni')
    viewed = models.PositiveIntegerField(default=1,verbose_name="Ko'rilganlar soni",help_text="Ko'rilganlar soni")
    shared = models.PositiveIntegerField(default=1,verbose_name="Ulashilganlar soni",help_text="Ulashilganlar soni")
    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Kitoblar"
        verbose_name = "Kitob "
        verbose_name_plural = "Kitoblar "

class Comments(models.Model):
    comment = models.TextField(verbose_name="Izoh",help_text="Izoh yozing")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    reply = models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)
    writed = models.DateTimeField(auto_now_add=True,verbose_name="Izoh yozilgan vaqt",help_text="Izoh yozilgan vaqt")

    def __str__(self):
        return f"{self.book.name} kitobiga izohlar"
    class Meta:
        db_table = "Izohlar"
        verbose_name = "Izoh "
        verbose_name_plural = "Izohlar "


