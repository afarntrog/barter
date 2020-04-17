import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime
from taggit.managers import TaggableManager

from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


# If you only inherit GenericUUIDTaggedItemBase, you need to define  a tag field.
#  e.g. tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)
class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

# Stores info about the listed product
class Product(models.Model):
    uid = models.CharField(primary_key=True, max_length=250, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=250, blank=False, null=True)
    desc = models.TextField(max_length=250, blank=False, null=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager(
        through=UUIDTaggedItem)  # https://django-taggit.readthedocs.io/en/latest/custom_tagging.html#genericuuidtaggeditembase

    # we can use get_absolute_url directly which already has the pk passed in.
    # Like so :: <h2><a href="{{ book.get_absolute_url }}">{{ book.title }}</a></h2>
    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.uid)])

# Many to one: Stores images for each product
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images/')

# Count how many times the product was viewed
class ProductViewCount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_view_count')
    ip = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

# Stores Favorite list
class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_favorites') # Use this related_name if you want to get all the users who favorited a specific product
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_favorites')