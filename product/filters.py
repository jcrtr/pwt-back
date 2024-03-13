import django_filters

from .models import Product


class StateFilter(django_filters.FilterSet):
    use = django_filters.CharFilter(
        name='use__name',
        lookup_type='contains',
    )

    class Meta:
        model = Product
        fields = ('name', 'use')
