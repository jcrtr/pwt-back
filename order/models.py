import uuid

from django.db import models


# Create your models here.
class Order(models.Model):
    __tablename__ = 'order'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.PositiveIntegerField(blank=True, unique=True)

    first_name = models.CharField(blank=True)
    last_name = models.CharField()
    email = models.EmailField()
    tel = models.CharField()

    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house = models.CharField(max_length=200)

    index = models.PositiveIntegerField()
