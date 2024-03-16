# Generated by Django 5.0.3 on 2024-03-15 17:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0027_alter_ssubcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='category.category', to_field='slug'),
        ),
        migrations.CreateModel(
            name='TwoSubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, verbose_name='НАЗВАНИЕ')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='ОПИСАНИЕ')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
                ('img', models.ImageField(blank=True, upload_to='', verbose_name='IMG')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two_sub_categories', to='category.subcategory', to_field='slug')),
            ],
            options={
                'verbose_name': 'ПодКатегория 2',
                'verbose_name_plural': 'ПодКатегории 2',
            },
        ),
        migrations.DeleteModel(
            name='SSubCategory',
        ),
    ]