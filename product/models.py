import uuid

from ckeditor.fields import RichTextField
from django.db import models

from category.models import Category, Use, SubCategory, TwoSubCategory


class ProductImage(models.Model):
    __tablename__ = 'product_img'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='public/img/product/')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'


class Product(models.Model):
    __tablename__ = 'product'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    priority = models.PositiveIntegerField('ПРИОРИТЕТ', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    two_sub_category = models.ForeignKey(TwoSubCategory, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    uses = models.ManyToManyField(Use, related_name='ОБЛАСТЬ', blank=True)
    name = models.CharField('НАИМЕНОВАНИЕ', max_length=200)
    short_description = models.TextField('ОПИСАНИЕ КРАТКОЕ', max_length=200, default='Описание')
    description = RichTextField('ОПИСАНИЕ')
    slug = models.SlugField('URL', max_length=50, unique=True)
    price = models.PositiveBigIntegerField('ЦЕНА')
    sale = models.PositiveIntegerField('СКИДКА %', default=0, null=True, blank=True)
    tag_one = models.CharField('ТЕГ 1', max_length=200, null=True, blank=True)
    tag_two = models.CharField('ТЕГ 2', max_length=200, null=True, blank=True)
    recommend = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name='Рекомендации',
    )
    repair = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name='Принадлежности',
    )

    images = models.ManyToManyField(ProductImage, related_name='КАРТИНКИ', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Сharacteristic(models.Model):
    __tablename__ = 'product_characteristic'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('ИМЯ', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class СharacteristicItem(models.Model):
    __tablename__ = 'product_characteristic_items'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic = models.ForeignKey(Сharacteristic, max_length=200, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='characteristics', on_delete=models.CASCADE)
    value = models.CharField('Значение', max_length=200)

    class Meta:
        verbose_name = 'Характеристика Продукта'
        verbose_name_plural = 'Характеристики Продукта'