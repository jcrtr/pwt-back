from rest_framework import serializers

from .filters import StateFilter
from .models import Product, СharacteristicItem, ProductImage


class СharacteristicItemSerializer(serializers.ModelSerializer):
    characteristic = serializers.CharField(source='characteristic.name')
    class Meta:
        model = СharacteristicItem
        fields = ['characteristic', 'value']


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, use):
        # returning image url if there is an image else blank string
        return 'https://pwt.reptiloid.space' + use.image.url if use.image else ''
    class Meta:
        model = ProductImage
        ordering = ['-main']
        fields = ['image', 'name', 'main']


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'price',
            'sale',
            'tag_one',
            'tag_two',
            'images',
            # 'category'
        ]
        filter_class = StateFilter


class ProductDetailSerializer(serializers.ModelSerializer):
    recommend = ProductSerializer(many=True)
    characteristics = СharacteristicItemSerializer(many=True)
    repair = ProductSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['id']
