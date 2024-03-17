from django.contrib import admin

from .models import Product, СharacteristicItem, Сharacteristic


class СharacteristicItemInline(admin.TabularInline):
    model = СharacteristicItem
    extra = 0


class СharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'priority', 'price', 'ch')
    # list_editable = ('category', 'sub_category', 'two_sub_category')
    # list_editable = ('repair',)
    search_fields = ['slug',]
    fieldsets = [
        ('Информация',
         {'fields': ['is_active', 'is_visible', 'category', 'sub_category', 'two_sub_category', 'name', 'description', 'slug', 'img', 'priority', ]}),
        ('Стоимость', {'fields': ['price', 'sale']}),
        ('Области применения', {'fields': ['uses']}),
        ('Рекомендации', {'fields': ['recommend']}),
        ('Принадлежности', {'fields': ['repair']}),
        ('Теги', {'fields': ['tag_one', 'tag_two']}),
    ]
    inlines = [СharacteristicItemInline]
    filter_horizontal = ('recommend', 'uses', 'repair')
    list_filter = ['uses__slug', 'category__slug']

    def ch(self, obj):
        return [characteristic.characteristic.name for characteristic in obj.characteristics.all()]


admin.site.register(Product, ProductAdmin)
admin.site.register(Сharacteristic, СharacteristicAdmin)
