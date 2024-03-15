from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'priority', 'category', 'sub_category')
    fieldsets = [
        ('Информация',
         {'fields': ['is_active', 'category', 'sub_category', 'name', 'description', 'slug', 'img', 'priority', ]}),
        ('Стоимость', {'fields': ['price', 'sale']}),
        ('Области применения', {'fields': ['uses']}),
        ('Рекомендации', {'fields': ['recommend']}),

        ('Теги',
         {'fields': ['tag_one', 'tag_two']}),

        ('Основные данные', {'fields': [
            'voltage_value', 'frequency_value', 'power_value',
            'heater_power_value', 'extruder_power_value',
            'working_frequency_value', 'available_frequency_value',
            'weight_value', 'engine_name'
        ]}),

        ('Параметры сварки', {
            'fields': ('welding_speed', 'heating_temperature', 'welding_temperature',
                       'extrusion_chamber_heating_temperature', 'operating_temperature',
                       'working_temperature_range', 'storage_temperature_range',
                       'welding_material_thickness', 'welding_surface_slope',
                       'rod_diameter', 'welded_rod_diameter', 'welding_zone')
        }),
        ('Ширина сварки', {
            'fields': ('weld_width', 'possible_weld_width', 'possible_strip_width',
                       'overlap_width', 'lap_width', 'workbench_width', 'rollers')
        }),
        ('Параметры воздуха', {
            'fields': ('working_pressure', 'compressor', 'air_flow_rate', 'air_pressure')
        }),
        ('Дополнительные характеристики', {
            'fields': ('additional_features', 'based_on_drill', 'head_diameter',
                       'setting_mode', 'handle', 'clamp_distance', 'voltage_amplification',
                       'range_value', 'size_value', 'vacuum_degree', 'noise_level',
                       'vacuum_chamber_area', 'relative_humidity', 'operation_mode',
                       'included_in_package')
        }),
    ]
    filter_horizontal = ('recommend', 'uses')


admin.site.register(Product, ProductAdmin)
