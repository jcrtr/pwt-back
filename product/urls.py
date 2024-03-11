from django.urls import path
from .views import ProductsList, ProductDetails

urlpatterns = [
    path('products/', ProductsList.as_view(), name='category-list'),
    path('product/<slug>', ProductDetails.as_view(), name='product-detail'),
]
