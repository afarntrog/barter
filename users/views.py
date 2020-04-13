from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Profile, ProfileViewCount

from core.models import Product, ProductViewCount


# Create your views here.


def home(request):
    return render(request, 'templates/app-marketplace/app-description.html', context={})


def profile(request):
    user = get_user_model().objects.get(username='aaron')
    user.products.all()
    view_count = record_view(request, '7d517151-d63f-49ed-8cd6-4094eef7b697')
    ip = request.META['REMOTE_ADDR']
    return render(request, 'users/author.html', {'user': user, 'ip': ip, 'total_views': view_count})


class ProfileDetail(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=get_user_model().objects.get(username=kwargs['username']))
        record_view(request, profile.id)
        return render(request, 'users/author.html', {'profile': profile})


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
