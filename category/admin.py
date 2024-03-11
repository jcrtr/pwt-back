from django.contrib import admin

from .models import Category, Use, SubCategory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'slug')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'category', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class UseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, CategoryAdmin)
admin.site.register(Use, CategoryAdmin)
