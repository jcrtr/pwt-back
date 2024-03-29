# Generated by Django 5.0.3 on 2024-03-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0025_use_short_name'),
        ('product', '0019_product_additional_features_product_air_flow_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additional_features',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Дополнительные функции'),
        ),
        migrations.AlterField(
            model_name='product',
            name='air_flow_rate',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расход воздуха'),
        ),
        migrations.AlterField(
            model_name='product',
            name='air_pressure',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Давление воздуха'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available_frequency_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Доступная частота'),
        ),
        migrations.AlterField(
            model_name='product',
            name='clamp_distance',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расстояние между зажимами'),
        ),
        migrations.AlterField(
            model_name='product',
            name='compressor',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Компрессор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='extruder_power_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Мощность экструдера'),
        ),
        migrations.AlterField(
            model_name='product',
            name='extrusion_chamber_heating_temperature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Температура нагрева экструзионной камеры'),
        ),
        migrations.AlterField(
            model_name='product',
            name='frequency_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Частота'),
        ),
        migrations.AlterField(
            model_name='product',
            name='handle',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Рукоять'),
        ),
        migrations.AlterField(
            model_name='product',
            name='head_diameter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Диаметр головки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='heater_power_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Мощность нагревателя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='heating_temperature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Температура нагрева'),
        ),
        migrations.AlterField(
            model_name='product',
            name='included_in_package',
            field=models.CharField(blank=True, default=False, max_length=200, null=True, verbose_name='В комплекте'),
        ),
        migrations.AlterField(
            model_name='product',
            name='lap_width',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ширина перехлеста'),
        ),
        migrations.AlterField(
            model_name='product',
            name='noise_level',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уровень шума'),
        ),
        migrations.AlterField(
            model_name='product',
            name='operating_temperature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Температура эксплуатации'),
        ),
        migrations.AlterField(
            model_name='product',
            name='operation_mode',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Режим работы'),
        ),
        migrations.AlterField(
            model_name='product',
            name='overlap_width',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ширина нахлеста'),
        ),
        migrations.AlterField(
            model_name='product',
            name='possible_strip_width',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Возможная ширина ленты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='possible_weld_width',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Возможная ширина шва'),
        ),
        migrations.AlterField(
            model_name='product',
            name='power_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Мощность'),
        ),
        migrations.AlterField(
            model_name='product',
            name='range_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Диапазон'),
        ),
        migrations.AlterField(
            model_name='product',
            name='recommend',
            field=models.ManyToManyField(blank=True, to='product.product', verbose_name='Рекомендации'),
        ),
        migrations.AlterField(
            model_name='product',
            name='relative_humidity',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Относительная влажность'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rod_diameter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Диаметр прутка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rollers',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Валики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='setting_mode',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Режим настройки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage_temperature_range',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Диапазон температуры хранения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uses',
            field=models.ManyToManyField(blank=True, related_name='ОБЛАСТЬ', to='category.use'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vacuum_chamber_area',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Площадь вакуумного колпака'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vacuum_degree',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Степень разряжения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='voltage_amplification',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Усиление напряжения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='voltage_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Напряжение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weld_width',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ширина шва'),
        ),
        migrations.AlterField(
            model_name='product',
            name='welded_rod_diameter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Диаметр сварного прутка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='welding_material_thickness',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Толщина материала, подлежащего сварке'),
        ),
        migrations.AlterField(
            model_name='product',
            name='welding_speed',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Скорость сварки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='welding_surface_slope',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уклон свариваемой поверхности'),
        ),
        migrations.AlterField(
            model_name='product',
            name='welding_temperature',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Температура сварки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='welding_zone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Зона сварки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='workbench_width',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ширина рабочего стола'),
        ),
        migrations.AlterField(
            model_name='product',
            name='working_frequency_value',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Рабочая частота'),
        ),
        migrations.AlterField(
            model_name='product',
            name='working_pressure',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Рабочее давление'),
        ),
        migrations.AlterField(
            model_name='product',
            name='working_temperature_range',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Диапазон рабочих температур'),
        ),
    ]
