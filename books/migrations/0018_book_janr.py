# Generated by Django 4.0.5 on 2022-07-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='janr',
            field=models.ForeignKey(blank=True, help_text='Kitob janr(lar)i ni kiriting', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='janr', to='books.genres', verbose_name='Kitob janr(lar)i'),
        ),
    ]
