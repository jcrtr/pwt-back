from rest_framework import serializers
from .models import Category, Use


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug']


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = ['id', 'name', 'description', 'slug']
