# Generated by Django 5.0.3 on 2024-03-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_remove_product_included_in_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='included_in_package',
            field=models.CharField(blank=True, default=False, max_length=200, null=True, verbose_name='В комплекте'),
        ),
    ]
