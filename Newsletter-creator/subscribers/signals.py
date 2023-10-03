from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Subscriber, Unsubscriber


@receiver(pre_save, sender=Subscriber)
def my_callback(sender, instance, **kwargs):
    try:
        unsubscriber = Unsubscriber.objects.get(email=instance.email)
        unsubscriber.delete()
    except Unsubscriber.DoesNotExist:
        pass
