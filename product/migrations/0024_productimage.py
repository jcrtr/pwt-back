# Generated by Django 5.0.3 on 2024-03-15 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_product_tag_one_product_tag_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('my_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]
