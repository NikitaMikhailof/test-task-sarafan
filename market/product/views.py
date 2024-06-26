import os

from PIL import Image
from django.shortcuts import render
from pytils.translit import slugify
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from market.settings import BASE_DIR
from product.models import Category, Product
from product.paginations import StandardPagination
from product.serialazier import CategorySerializer, ProductSerializer, CategoryListSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        return CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardPagination
