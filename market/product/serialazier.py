from pytils.translit import slugify
from rest_framework import serializers

from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug',)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'category')
        read_only_fields = ('slug',)


class CategoryListSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'category', 'subcategories')
        read_only_fields = ('slug',)


class ProductSerializer(serializers.ModelSerializer):
    _category = serializers.SlugRelatedField(slug_field='title', read_only=True, source='category')

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('slug', 'medium_img', 'small_img')