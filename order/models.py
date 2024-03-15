import uuid

from django.db import models
from django.utils import timezone

from product.models import Product


# Create your models here.
class Order(models.Model):
    __tablename__ = 'order'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.PositiveIntegerField(blank=True, unique=True)

    first_name = models.CharField(blank=True, max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    tel = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, through='OrderItem')

    created_at = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_total_amount(self):
        self.total_amount = sum(item.get_item_total() for item in self.items.all())
        self.save()


class OrderDelivery(models.Model):
    __tablename__ = 'order_delivery'

    order = models.OneToOneField(Order, related_name='delivery', on_delete=models.CASCADE)

    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house = models.CharField(max_length=200)

    index = models.PositiveIntegerField()


class OrderItem(models.Model):
    __tablename__ = 'order_item'

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='slug')
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"

    def save(self, *args, **kwargs):
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def get_item_total(self):
        return self.quantity * self.product.price