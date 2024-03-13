import uuid

from ckeditor.fields import RichTextField
from django.db import models

from category.models import Category, Use, SubCategory


class Product(models.Model):
    __tablename__ = 'product'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    priority = models.PositiveIntegerField('ПРИОРИТЕТ', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    uses = models.ManyToManyField(Use, related_name='ОБЛАСТЬ', blank=True, null=True)
    name = models.CharField('НАИМЕНОВАНИЕ', max_length=200)
    short_description = models.TextField('ОПИСАНИЕ КРАТКОЕ', max_length=200, default='Описание')
    description = RichTextField('ОПИСАНИЕ')
    slug = models.SlugField('URL', max_length=50, unique=True)
    img = models.ImageField('IMG', null=True, blank=True,)
    price = models.PositiveBigIntegerField('ЦЕНА')
    sale = models.PositiveIntegerField('СКИДКА %', default=0, null=True, blank=True)
    recommend = models.ManyToManyField(
        "self",
        blank=True,
        null=True,
        verbose_name='Рекомендации',
    )

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'