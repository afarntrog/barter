from django.urls import path, include
from .views import profile, ProfileDetail, SettingsView, home
# ...profile
urlpatterns = [
    path('', home, name='home'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('profile', profile, name='profile'),
    path('profile/<username>/', ProfileDetail.as_view(), name='profile_detail'),
]
