from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import  CustomUserChangeForm, CustomUserCreationForm
from .models import  CustomUser, Profile, Address

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    readonly_fields = ('updated_at',)
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]



admin.site.register(CustomUser, CustomUserAdmin)
# add the profile instance as an inline
admin.site.register(Address)