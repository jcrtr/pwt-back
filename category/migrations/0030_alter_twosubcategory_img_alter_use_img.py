# Generated by Django 5.0.3 on 2024-03-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0029_alter_category_img_alter_twosubcategory_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twosubcategory',
            name='img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='IMG'),
        ),
        migrations.AlterField(
            model_name='use',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uses/', verbose_name='IMG'),
        ),
    ]
