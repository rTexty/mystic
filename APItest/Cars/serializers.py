from rest_framework import serializers
from .models import Car, Brand, Category

class CarSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brands.name')  # Serializer for the Brand model
    category = serializers.CharField(source='cat.name')  # Serializer for the Category model

    class Meta:
        model = Car
        fields = ('year', 'brand', 'category')