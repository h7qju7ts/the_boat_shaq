from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.dispatch import receiver

from .models import UserProfile
from django.apps import AppConfig

User = get_user_model()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)   

    else:
        UserProfile.objects.get_or_create(user=instance)


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    def ready(self):
        import profiles.signals    
