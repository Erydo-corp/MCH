from rest_framework import serializers

from .models import Product, Category


class ProductListSerializers(serializers.ModelSerializer):
    """Список товаров"""

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializers(serializers.ModelSerializer):
    """Товар детально"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializers(serializers.ModelSerializer):
    """Категории товаров"""

    class Meta:
        model = Category
        exclude = ['slug']
