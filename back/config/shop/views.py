from rest_framework import generics

from .models import Product, Category
from shop.serializers import ProductListSerializers, ProductDetailSerializers, CategoryListSerializers


class ProductListView(generics.ListAPIView):
    """Вывод списка товаров"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializers


class ProductDetailView(generics.RetrieveAPIView):
    """Продукт детально"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductDetailSerializers


class CategoryListView(generics.ListAPIView):
    """Список категорий"""
    # Нужно подумать над выводом продуктов по категориям
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
