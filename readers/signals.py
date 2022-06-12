from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Kitobxon
@receiver(post_save, sender=User)
def create_kitobxon(sender, instance, created, **kwargs):
    if created:
        Kitobxon.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_kitobxon(sender, instance, **kwargs):
        instance.kitobxon.save()

