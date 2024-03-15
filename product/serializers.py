from rest_framework import serializers

from .filters import StateFilter
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'price',
            # 'category'
        ]
        filter_class = StateFilter


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']
