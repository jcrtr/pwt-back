# Generated by Django 5.0.3 on 2024-03-11 11:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0015_alter_subcategory_id_alter_subcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, primary_key=True, serialize=False, unique=True, verbose_name='URL'),
        ),
    ]
