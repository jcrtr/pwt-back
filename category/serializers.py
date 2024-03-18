from rest_framework import serializers
from .models import Category, Use, SubCategory, TwoSubCategory


class TwoSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoSubCategory
        fields = ['id', 'name', 'description', 'slug']


class SubCategorySerializer(serializers.ModelSerializer):
    two_sub_categories = TwoSubCategorySerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'slug', 'two_sub_categories']


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)
    img = serializers.ImageField(use_url=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'img', 'description', 'slug', 'sub_categories']


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = ['id', 'name', 'img', 'description', 'slug', 'short_name']
