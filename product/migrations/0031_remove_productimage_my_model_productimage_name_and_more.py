# Generated by Django 5.0.3 on 2024-03-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_product_repair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='my_model',
        ),
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='public/img/product/'),
        ),
    ]