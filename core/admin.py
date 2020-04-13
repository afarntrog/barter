from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, ProductImages


# Register your models here

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    can_delete = False


class CustomProduct(admin.ModelAdmin):
    inlines = (ProductImagesInline,)
    model = Product
    list_display = ('owner', 'title', 'desc', 'created_at', 'tags')


admin.site.register(Product, CustomProduct)
# admin.site.register(Product)