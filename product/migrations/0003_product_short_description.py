# Generated by Django 5.0.3 on 2024-03-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(max_length=200, null=True, verbose_name='ОПИСАНИЕ КРАТКОЕ'),
        ),
    ]
