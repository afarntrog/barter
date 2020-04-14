from django.urls import path, include
from .views import profile, ProfileDetail
# ...profile
urlpatterns = [
    path('', profile, name='home'),
    path('profile', profile, name='profile'),
    path('profile/<username>/', ProfileDetail.as_view(), name='profile_detail'),
]
