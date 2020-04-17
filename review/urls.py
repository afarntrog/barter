from django.urls import path, include
from .views import ReviewUser

urlpatterns = [
    path('<uuid:pk>',  ReviewUser.as_view(), name='review'),
]
