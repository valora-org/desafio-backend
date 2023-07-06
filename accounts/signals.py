from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser as User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User, weak=False)
def report_uploaded(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)