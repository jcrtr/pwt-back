# Generated by Django 5.0.3 on 2024-03-11 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0021_alter_category_id_alter_category_slug'),
        ('product', '0011_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.subcategory'),
        ),
    ]
