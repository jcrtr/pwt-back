# Generated by Django 5.0.3 on 2024-03-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_rename_сharacteristicsitems_сharacteristicitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='СharacteristicItems',
            new_name='СharacteristicItem',
        ),
    ]
