from .models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gte', 'lte']
            }

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock=0)
