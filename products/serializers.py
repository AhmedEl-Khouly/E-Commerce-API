from .models import Product
from categories.models import Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'slug', 'description', 'price', 'stock']
        extra_kwargs = {
            'slug': {'read_only': True},
            'category': {'read_only': True},
        }
    def get_in_stock(self, obj):
        return obj.stock > 0