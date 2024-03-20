import uuid

from ckeditor.fields import RichTextField
from django.db import models

from category.models import Category, Use, SubCategory, TwoSubCategory


class ProductImage(models.Model):
    __tablename__ = 'product_img'

    image = models.ImageField(upload_to='public/img/product/')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'


class Product(models.Model):
    __tablename__ = 'product'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    priority = models.PositiveIntegerField('ПРИОРИТЕТ', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    two_sub_category = models.ForeignKey(TwoSubCategory, on_delete=models.CASCADE, null=True, blank=True, to_field='slug')
    uses = models.ManyToManyField(Use, related_name='ОБЛАСТЬ', blank=True)
    name = models.CharField('НАИМЕНОВАНИЕ', max_length=200)
    short_description = models.TextField('ОПИСАНИЕ КРАТКОЕ', max_length=200, default='Описание')
    description = RichTextField('ОПИСАНИЕ')
    slug = models.SlugField('URL', max_length=50, unique=True)
    price = models.PositiveBigIntegerField('ЦЕНА')
    sale = models.PositiveIntegerField('СКИДКА %', default=0, null=True, blank=True)
    tag_one = models.CharField('ТЕГ 1', max_length=200, null=True, blank=True)
    tag_two = models.CharField('ТЕГ 2', max_length=200, null=True, blank=True)
    recommend = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name='Рекомендации',
    )
    repair = models.ManyToManyField(
        "self",
        blank=True,
        verbose_name='Принадлежности',
    )

    images = models.ManyToManyField(ProductImage, related_name='КАРТИНКИ', blank=True)

    # Характеристики

    # voltage_value = models.CharField(verbose_name="Напряжение", max_length=200, null=True, blank=True)
    # frequency_value = models.CharField(verbose_name="Частота", max_length=200, null=True, blank=True)
    # power_value = models.CharField(verbose_name="Мощность", max_length=200, null=True, blank=True)
    # heater_power_value = models.CharField(verbose_name="Мощность нагревателя", max_length=200, null=True, blank=True)
    # extruder_power_value = models.CharField(verbose_name="Мощность экструдера", max_length=200, null=True, blank=True)
    # working_frequency_value = models.CharField(verbose_name="Рабочая частота", max_length=200, null=True, blank=True)
    # available_frequency_value = models.CharField(verbose_name="Доступная частота", max_length=200, null=True,
    #                                              blank=True)
    # weight_value = models.CharField(verbose_name="Вес", max_length=200, null=True, blank=True)
    # engine_name = models.CharField(max_length=100, verbose_name="Двигатель", null=True, blank=True)
    #
    # welding_speed = models.CharField(verbose_name="Скорость сварки", max_length=200, null=True, blank=True)
    # heating_temperature = models.CharField(verbose_name="Температура нагрева", max_length=200, null=True, blank=True)
    # welding_temperature = models.CharField(verbose_name="Температура сварки", max_length=200, null=True, blank=True)
    # extrusion_chamber_heating_temperature = models.CharField(verbose_name="Температура нагрева экструзионной камеры",
    #                                                          max_length=200, null=True, blank=True)
    # operating_temperature = models.CharField(verbose_name="Температура эксплуатации", max_length=200, null=True,
    #                                          blank=True)
    # working_temperature_range = models.CharField(max_length=200, verbose_name="Диапазон рабочих температур", null=True,
    #                                              blank=True)
    # storage_temperature_range = models.CharField(max_length=200, verbose_name="Диапазон температуры хранения",
    #                                              null=True, blank=True)
    # welding_material_thickness = models.CharField(verbose_name="Толщина материала, подлежащего сварке", max_length=200,
    #                                               null=True, blank=True)
    # welding_surface_slope = models.CharField(verbose_name="Уклон свариваемой поверхности", max_length=200, null=True,
    #                                          blank=True)
    # rod_diameter = models.CharField(verbose_name="Диаметр прутка", max_length=200, null=True, blank=True)
    # welded_rod_diameter = models.CharField(verbose_name="Диаметр сварного прутка", max_length=200, null=True,
    #                                        blank=True)
    # welding_zone = models.CharField(max_length=200, verbose_name="Зона сварки", null=True, blank=True)

    # weld_width = models.CharField(verbose_name="Ширина шва", max_length=200, null=True, blank=True)
    # possible_weld_width = models.CharField(verbose_name="Возможная ширина шва", max_length=200, null=True, blank=True)
    # possible_strip_width = models.CharField(verbose_name="Возможная ширина ленты", max_length=200, null=True,
    #                                         blank=True)
    # overlap_width = models.CharField(verbose_name="Ширина нахлеста", max_length=200, null=True, blank=True)
    # lap_width = models.CharField(verbose_name="Ширина перехлеста", max_length=200, null=True, blank=True)
    # workbench_width = models.CharField(verbose_name="Ширина рабочего стола", max_length=200, null=True, blank=True)
    # rollers = models.CharField(max_length=200, verbose_name="Валики", null=True, blank=True)

    # working_pressure = models.CharField(verbose_name="Рабочее давление", max_length=200, null=True, blank=True)
    # compressor = models.CharField(max_length=200, verbose_name="Компрессор", null=True, blank=True)
    # air_flow_rate = models.CharField(verbose_name="Расход воздуха", max_length=200, null=True, blank=True)
    # air_pressure = models.CharField(verbose_name="Давление воздуха", max_length=200, null=True, blank=True)

    # additional_features = models.CharField(max_length=200, verbose_name="Дополнительные функции", null=True, blank=True)
    # based_on_drill = models.BooleanField(default=False, verbose_name="На базе дрели", null=True, blank=True)
    # head_diameter = models.CharField(verbose_name="Диаметр головки", max_length=200, null=True, blank=True)
    # setting_mode = models.CharField(max_length=200, verbose_name="Режим настройки", null=True, blank=True)
    # handle = models.CharField(max_length=200, verbose_name="Рукоять", null=True, blank=True)
    # clamp_distance = models.CharField(verbose_name="Расстояние между зажимами", max_length=200, null=True, blank=True)
    # voltage_amplification = models.CharField(verbose_name="Усиление напряжения", max_length=200, null=True, blank=True)
    # range_value = models.CharField(max_length=200, verbose_name="Диапазон", null=True, blank=True)
    # size_value = models.CharField(max_length=200, verbose_name="Размер", null=True, blank=True)
    # vacuum_degree = models.CharField(verbose_name="Степень разряжения", max_length=200, null=True, blank=True)
    # noise_level = models.CharField(verbose_name="Уровень шума", max_length=200, null=True, blank=True)
    # vacuum_chamber_area = models.CharField(verbose_name="Площадь вакуумного колпака", max_length=200, null=True,
    #                                        blank=True)
    # relative_humidity = models.CharField(verbose_name="Относительная влажность", max_length=200, null=True, blank=True)
    # operation_mode = models.CharField(max_length=200, verbose_name="Режим работы", null=True, blank=True)
    # included_in_package = models.CharField(default=False, verbose_name="В комплекте", max_length=200, null=True,
    #                                        blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'





class Сharacteristic(models.Model):
    __tablename__ = 'product_characteristic'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('ИМЯ', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class СharacteristicItem(models.Model):
    __tablename__ = 'product_characteristic_items'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic = models.ForeignKey(Сharacteristic, max_length=200, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='characteristics', on_delete=models.CASCADE)
    value = models.CharField('Значение', max_length=200)

    class Meta:
        verbose_name = 'Характеристика Продукта'
        verbose_name_plural = 'Характеристики Продукта'