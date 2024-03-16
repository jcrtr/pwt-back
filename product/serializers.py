from rest_framework import serializers

from .filters import StateFilter
from .models import Product, СharacteristicItem


class СharacteristicItemSerializer(serializers.ModelSerializer):
    characteristic = serializers.CharField(source='characteristic.name')
    class Meta:
        model = СharacteristicItem
        fields = ['characteristic', 'value']


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'price',
            'sale',
            'tag_one',
            'tag_two',
            # 'category'
        ]
        filter_class = StateFilter


class ProductDetailSerializer(serializers.ModelSerializer):
    recommend = ProductSerializer(many=True)
    characteristics = СharacteristicItemSerializer(many=True)
    class Meta:
        model = Product
        exclude = ['id']
