# Generated by Django 4.0.5 on 2022-06-12 06:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_uploaded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='writed',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 12, 6, 19, 30, 953905, tzinfo=utc), help_text='Izoh yozilgan vaqt', verbose_name='Izoh yozilgan vaqt'),
            preserve_default=False,
        ),
    ]
