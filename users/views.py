from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Profile, ProfileViewCount

from core.models import Product, ProductViewCount


# Create your views here.


def home(request):
    return render(request, 'core/index.html', context={})


def profile(request):
    user = get_user_model().objects.get(username=request.user.username)
    user.products.all()
    # view_count = record_view(request, '7d517151-d63f-49ed-8cd6-4094eef7b697')
    ip = request.META['REMOTE_ADDR']
    return render(request, 'users/author.html', {'user': user, 'ip': ip, })


# Settings page
class SettingsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/settings.html', {})


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=get_user_model().objects.get(username=kwargs['username']))
        user = get_user_model().objects.get(username=kwargs['username'])
        view_count = record_view(request, profile.id)
        return render(request, 'users/author.html', {'profile': profile, 'user': user, 'total_views': view_count})


# Count unique views
def record_view(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    if not ProfileViewCount.objects.filter(
            profile=profile,
            ip=request.META['REMOTE_ADDR']):
        view = ProfileViewCount(profile=profile,
                                ip=request.META['REMOTE_ADDR'], )
        view.save()
    return ProfileViewCount.objects.filter(profile=profile).count()
