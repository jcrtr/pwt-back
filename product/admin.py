from django.contrib import admin

from .models import Product, СharacteristicItem, Сharacteristic, ProductImage


class СharacteristicItemInline(admin.TabularInline):
    model = СharacteristicItem
    extra = 0


class СharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductImagesAdmin(admin.ModelAdmin):
    model = ProductImage
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'priority', 'price', 'sale', 'ch')
    # list_editable = ('category', 'sub_category', 'two_sub_category')
    # list_editable = ('price', 'sale')
    search_fields = ['slug', 'name']
    fieldsets = [
        ('Информация',
         {'fields': ['is_active', 'is_visible', 'category', 'sub_category', 'two_sub_category', 'name', 'description', 'slug', 'priority', ]}),
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
