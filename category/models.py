import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    __tablename__ = 'category'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField('НАЗВАНИЕ', max_length=200)
    description = models.TextField('ОПИСАНИЕ', null=True, blank=True)
    slug = models.SlugField('URL', max_length=50, unique=True)
    img = models.ImageField('IMG', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    __tablename__ = 'sub_category'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='КАТЕГОРИЯ', null=True, to_field='slug')
    name = models.CharField('НАЗВАНИЕ', max_length=200)
    description = models.TextField('ОПИСАНИЕ', max_length=200, null=True, blank=True)
    slug = models.SlugField('URL', max_length=50, unique=True, blank=True)
    img = models.ImageField('IMG', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ПодКатегория'
        verbose_name_plural = 'ПодКатегории'


class Use(models.Model):
    __tablename__ = 'use'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField('НАЗВАНИЕ', max_length=200)
    short_name = models.CharField('КОРОТКИЕ НАЗВАНИЕ', max_length=200, null=True)
    description = models.TextField('ОПИСАНИЕ')
    slug = models.SlugField('URL', max_length=50, unique=True)
    img = models.ImageField('IMG', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область применения'
        verbose_name_plural = 'Области применения'