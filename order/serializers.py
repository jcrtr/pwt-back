from rest_framework import serializers, viewsets

from .models import Order, OrderItem, OrderDelivery

# Сериализатор для элементов заказа
from rest_framework import serializers
from .models import Order, OrderDelivery, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'item_total']


class OrderDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDelivery
        fields = ['country', 'city', 'street', 'house', 'index']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # Вложенный сериализатор для обработки данных о товарах
    delivery = OrderDeliverySerializer(required=False)  # Вложенный сериализатор для обработки данных о доставке

    class Meta:
        model = Order
        fields = ['id', 'number', 'first_name', 'last_name', 'email', 'tel', 'created_at', 'total_amount', 'items',
                  'delivery']

    def create(self, validated_data):
        items_data = validated_data.pop('items')  # Извлекаем данные о товарах из входящих данных
        delivery_data = validated_data.pop('delivery')  # Извлекаем данные о доставке из входящих данных

        order = Order.objects.create(**validated_data)  # Создаем заказ
        if delivery_data:
            OrderDelivery.objects.create(order=order, **delivery_data)  # Создаем данные о доставке и связываем их с заказом

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)  # Создаем записи о товарах и связываем их с заказом

        return order
