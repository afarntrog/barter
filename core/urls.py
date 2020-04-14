
from django.urls import path, include
from .views import ProductDetail, PostProduct, ProductList
# ...profile
urlpatterns = [
    path('list', ProductList.as_view(), name='product_list'),
    path("<uuid:pk>", ProductDetail.as_view(), name="product_detail"),
    path('post/', PostProduct.as_view(), name='post_product'),
]

# ../tag/waterford...