# Generated by Django 4.0.5 on 2022-07-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, help_text='Kitob janr(lar)i ni kiriting', null=True, related_name='books', to='books.genres', verbose_name='Kitob janr(lar)i'),
        ),
    ]