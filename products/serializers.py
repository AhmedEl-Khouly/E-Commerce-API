from .models import Product
from rest_framework import serializers
from categories.serializers import CategorySerializer
from categories.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True
    )
    category_name = serializers.CharField(
        source='category.name', read_only=True
    )
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'slug', 'description', 'price', 'stock', 'category_name']
        extra_kwargs = {
            'slug': {'read_only': True},
        }