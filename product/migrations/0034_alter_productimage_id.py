# Generated by Django 5.0.3 on 2024-03-20 12:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_alter_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
