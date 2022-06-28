# Generated by Django 4.0.5 on 2022-06-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Kitob janr(lar)i ni kiriting', related_name='books', to='books.genres', verbose_name='Kitob janr(lar)i'),
        ),
    ]
