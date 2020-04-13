
from django.urls import path, include
from .views import ProductDetail
# ...profile
urlpatterns = [
    path("<uuid:pk>", ProductDetail.as_view(), name="product_detail"),
]

