from django.contrib import admin

from .models import Order, OrderItem, OrderDelivery


# Регистрация модели OrderItem в административном интерфейсе
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderDeliveryInline(admin.TabularInline):
    model = OrderDelivery
    extra = 1


# Регистрация модели Order в административном интерфейсе
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'total_amount']
    inlines = [OrderDeliveryInline, OrderItemInline]

