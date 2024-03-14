from rest_framework import serializers

from .filters import StateFilter
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # use = UseSerializer(many=True)
    class Meta:
        model = Product
        exclude = ['id']
        filter_class = StateFilter


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']
