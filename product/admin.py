from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'priority', 'category', 'sub_category')
    fieldsets = [
        ('Информация', {'fields': ['is_active', 'category', 'sub_category', 'name', 'description', 'slug', 'img', 'priority', ]}),
        ('Стоимость', {'fields': ['price', 'sale']}),
        ('Области применения', {'fields': ['use']}),
        ('Рекомендации', {'fields': ['recommend']}),
    ]
    filter_horizontal = ('recommend', 'use')


admin.site.register(Product, ProductAdmin)
