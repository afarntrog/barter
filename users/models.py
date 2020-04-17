from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.db.models.signals import post_save


##############
# Custome user model.
##############
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


##############
# Users Home Address
##############
class Address(models.Model):
    """Model to store addresses for accounts"""
    address_line1 = models.CharField("Address line 1", max_length=45)
    address_line2 = models.CharField("Address line 2", max_length=45, blank=True)
    zip_code = models.CharField("Postal Code", max_length=10)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField("State/Province", max_length=40, blank=False)
    country = models.CharField("Country", max_length=40, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city} {self.state} {self.country}"

    class Meta:
        verbose_name_plural = "Addresses"
        unique_together = ("address_line1", "address_line2", "zip_code",
                           "city", "state", "country")


##############
# Users Profile
##############
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/download.jpeg')
    phone = PhoneNumberField(
        blank=True)  # https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    bio = models.TextField(max_length=500, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


# Count how many times the profile was viewed
class ProfileViewCount(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_view_count')
    ip = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)


# Create a new profile automatically on signup.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)


class Review(models.Model):
    review = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.review[:30]

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
