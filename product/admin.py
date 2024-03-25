from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, СharacteristicItem, Сharacteristic, ProductImage


class СharacteristicItemInline(admin.TabularInline):
    model = СharacteristicItem
    extra = 0


class СharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductImagesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    model = ProductImage
    search_fields = ['name']
    list_display = ('name', 'preview', 'main')
    list_editable = ('main',)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name',  'is_visible', 'slug', 'priority', 'price', 'sale', 'ch', 'description')
    # list_editable = ('category', 'sub_category', 'two_sub_category')
    # list_editable = ('description',)
    search_fields = ['slug', 'name']
    fieldsets = [
        ('Информация',
         {'fields': ['is_active', 'is_visible', 'category', 'sub_category', 'two_sub_category', 'name', 'description',
                     'slug', 'priority', 'video_url']}),
        ('Миниатюра', {'fields': ['thump']}),
        ('Стоимость', {'fields': ['price', 'sale']}),
        ('Области применения', {'fields': ['uses']}),
        ('Рекомендации', {'fields': ['recommend']}),
        ('Принадлежности', {'fields': ['repair']}),
        ('Картинка', {'fields': ['images']}),
        ('Теги', {'fields': ['tag_one', 'tag_two']}),
    ]
    inlines = [СharacteristicItemInline]
    filter_horizontal = ('recommend', 'uses', 'repair', 'images')
    list_filter = ['uses__slug', 'category__slug']

    def ch(self, obj):
        return [use.name for use in obj.uses.all()]


admin.site.register(Product, ProductAdmin)
admin.site.register(Сharacteristic, СharacteristicAdmin)
admin.site.register(ProductImage, ProductImagesAdmin)
