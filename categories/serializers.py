from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        extra_kwargs = {
            'slug': {'read_only': True}
        }
        
    # def create(self, validated_data):
    #     category = Category.objects.create(**validated_data)
    #     return category