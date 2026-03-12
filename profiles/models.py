from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="userprofile"
    )
    default_full_name = models.CharField(max_length=100, blank=True)
    default_email = models.EmailField(blank=True)
    default_phone_number = models.CharField(max_length=20, blank=True)
    default_street_address1 = models.CharField(max_length=255, blank=True)
    default_street_address2 = models.CharField(max_length=255, blank=True)
    default_town_or_city = models.CharField(max_length=100, blank=True)
    default_county = models.CharField(max_length=100, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username