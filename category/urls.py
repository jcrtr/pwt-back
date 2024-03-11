from django.urls import path
from .views import CategoriesList, UseList, UseDetails

urlpatterns = [
    path('categories/', CategoriesList.as_view(), name='category-list'),
    path('uses/', UseList.as_view(), name='use-list'),
    path('use/<slug>', UseDetails.as_view(), name='use-detail'),
]
