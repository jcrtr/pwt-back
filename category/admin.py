from django.contrib import admin

from .models import Category, Use, SubCategory, TwoSubCategory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'slug')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category__slug']


class SSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category__slug']


class UseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'slug')
    list_filter = ['category__slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(TwoSubCategory, SSubCategoryAdmin)
admin.site.register(Use, CategoryAdmin)
