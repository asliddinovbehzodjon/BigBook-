# Generated by Django 4.0.5 on 2022-07-12 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='uploader',
        ),
    ]
