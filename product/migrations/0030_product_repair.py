# Generated by Django 5.0.3 on 2024-03-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_rename_сharacteristicitems_сharacteristicitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='repair',
            field=models.ManyToManyField(blank=True, to='product.product', verbose_name='Принадлежности'),
        ),
    ]
