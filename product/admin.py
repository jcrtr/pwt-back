from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'priority', 'category', 'sub_category')
    fieldsets = [
        ('Информация', {'fields': ['is_active', 'category', 'sub_category', 'name', 'description', 'slug', 'img', 'priority', ]}),
        ('Стоимость', {'fields': ['price', 'sale']}),
        ('Области применения', {'fields': ['uses']}),
        ('Рекомендации', {'fields': ['recommend']}),
    ]
    filter_horizontal = ('recommend', 'uses')


admin.site.register(Product, ProductAdmin)
