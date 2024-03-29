from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import StateFilter
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.filter(is_visible=True).order_by('-priority')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'uses__slug', 'sub_category', 'two_sub_category']
    search_fields = ['$name', '$category__name', '$uses__name', '$uses__short_name']
    filter_class = StateFilter


class ProductDetails(APIView):
    def get_object(self, slug):
        try:
            return Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, slug):

        data = self.get_object(slug)
        serializer = ProductDetailSerializer(data)
        return Response(serializer.data)
