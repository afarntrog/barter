
from django.urls import path, include
from .views import ProductDetail, PostProduct, ProductList, AddToFavorites
# ...profile
urlpatterns = [
    # Display products
    path('list', ProductList.as_view(), name='product_list'),
    path("<uuid:pk>", ProductDetail.as_view(), name="product_detail"),

    # Post product
    path('post/', PostProduct.as_view(), name='post_product'),

    path('fav/<uuid:pk>', AddToFavorites.as_view(), name='add_to_favorites'),


]

# ../tag/waterford...