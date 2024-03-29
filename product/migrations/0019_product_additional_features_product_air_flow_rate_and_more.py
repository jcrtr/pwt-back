# Generated by Django 5.0.3 on 2024-03-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_rename_use_product_uses'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additional_features',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дополнительные функции'),
        ),
        migrations.AddField(
            model_name='product',
            name='air_flow_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='Расход воздуха'),
        ),
        migrations.AddField(
            model_name='product',
            name='air_pressure',
            field=models.FloatField(blank=True, null=True, verbose_name='Давление воздуха'),
        ),
        migrations.AddField(
            model_name='product',
            name='available_frequency_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Доступная частота'),
        ),
        migrations.AddField(
            model_name='product',
            name='based_on_drill',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='На базе дрели'),
        ),
        migrations.AddField(
            model_name='product',
            name='clamp_distance',
            field=models.FloatField(blank=True, null=True, verbose_name='Расстояние между зажимами'),
        ),
        migrations.AddField(
            model_name='product',
            name='compressor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Компрессор'),
        ),
        migrations.AddField(
            model_name='product',
            name='engine_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Двигатель'),
        ),
        migrations.AddField(
            model_name='product',
            name='extruder_power_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Мощность экструдера'),
        ),
        migrations.AddField(
            model_name='product',
            name='extrusion_chamber_heating_temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура нагрева экструзионной камеры'),
        ),
        migrations.AddField(
            model_name='product',
            name='frequency_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Частота'),
        ),
        migrations.AddField(
            model_name='product',
            name='handle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Рукоять'),
        ),
        migrations.AddField(
            model_name='product',
            name='head_diameter',
            field=models.FloatField(blank=True, null=True, verbose_name='Диаметр головки'),
        ),
        migrations.AddField(
            model_name='product',
            name='heater_power_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Мощность нагревателя'),
        ),
        migrations.AddField(
            model_name='product',
            name='heating_temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура нагрева'),
        ),
        migrations.AddField(
            model_name='product',
            name='included_in_package',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='В комплекте'),
        ),
        migrations.AddField(
            model_name='product',
            name='lap_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина перехлеста'),
        ),
        migrations.AddField(
            model_name='product',
            name='noise_level',
            field=models.FloatField(blank=True, null=True, verbose_name='Уровень шума'),
        ),
        migrations.AddField(
            model_name='product',
            name='operating_temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура эксплуатации'),
        ),
        migrations.AddField(
            model_name='product',
            name='operation_mode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Режим работы'),
        ),
        migrations.AddField(
            model_name='product',
            name='overlap_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина нахлеста'),
        ),
        migrations.AddField(
            model_name='product',
            name='possible_strip_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Возможная ширина ленты'),
        ),
        migrations.AddField(
            model_name='product',
            name='possible_weld_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Возможная ширина шва'),
        ),
        migrations.AddField(
            model_name='product',
            name='power_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Мощность'),
        ),
        migrations.AddField(
            model_name='product',
            name='range_value',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Диапазон'),
        ),
        migrations.AddField(
            model_name='product',
            name='relative_humidity',
            field=models.FloatField(blank=True, null=True, verbose_name='Относительная влажность'),
        ),
        migrations.AddField(
            model_name='product',
            name='rod_diameter',
            field=models.FloatField(blank=True, null=True, verbose_name='Диаметр прутка'),
        ),
        migrations.AddField(
            model_name='product',
            name='rollers',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Валики'),
        ),
        migrations.AddField(
            model_name='product',
            name='setting_mode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Режим настройки'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_value',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер'),
        ),
        migrations.AddField(
            model_name='product',
            name='storage_temperature_range',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Диапазон температуры хранения'),
        ),
        migrations.AddField(
            model_name='product',
            name='vacuum_chamber_area',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь вакуумного колпака'),
        ),
        migrations.AddField(
            model_name='product',
            name='vacuum_degree',
            field=models.FloatField(blank=True, null=True, verbose_name='Степень разряжения'),
        ),
        migrations.AddField(
            model_name='product',
            name='voltage_amplification',
            field=models.FloatField(blank=True, null=True, verbose_name='Усиление напряжения'),
        ),
        migrations.AddField(
            model_name='product',
            name='voltage_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Напряжение'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='product',
            name='weld_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина шва'),
        ),
        migrations.AddField(
            model_name='product',
            name='welded_rod_diameter',
            field=models.FloatField(blank=True, null=True, verbose_name='Диаметр сварного прутка'),
        ),
        migrations.AddField(
            model_name='product',
            name='welding_material_thickness',
            field=models.FloatField(blank=True, null=True, verbose_name='Толщина материала, подлежащего сварке'),
        ),
        migrations.AddField(
            model_name='product',
            name='welding_speed',
            field=models.FloatField(blank=True, null=True, verbose_name='Скорость сварки'),
        ),
        migrations.AddField(
            model_name='product',
            name='welding_surface_slope',
            field=models.FloatField(blank=True, null=True, verbose_name='Уклон свариваемой поверхности'),
        ),
        migrations.AddField(
            model_name='product',
            name='welding_temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура сварки'),
        ),
        migrations.AddField(
            model_name='product',
            name='welding_zone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Зона сварки'),
        ),
        migrations.AddField(
            model_name='product',
            name='workbench_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина рабочего стола'),
        ),
        migrations.AddField(
            model_name='product',
            name='working_frequency_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Рабочая частота'),
        ),
        migrations.AddField(
            model_name='product',
            name='working_pressure',
            field=models.FloatField(blank=True, null=True, verbose_name='Рабочее давление'),
        ),
        migrations.AddField(
            model_name='product',
            name='working_temperature_range',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Диапазон рабочих температур'),
        ),
    ]
