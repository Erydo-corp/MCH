from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category
from shop.serializers import ProductListSerializers, ProductDetailSerializers, CategoryListSerializers


# from .service import ProductFilter


class ProductListView(generics.ListAPIView):
    """Вывод списка товаров"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializers
    # Фильтрация по категориям
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['category', ]


class ProductDetailView(generics.RetrieveAPIView):
    """Продукт детально"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductDetailSerializers


class CategoryListView(generics.ListAPIView):
    """Список категорий"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
