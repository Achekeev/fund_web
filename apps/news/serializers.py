from rest_framework.serializers import ModelSerializer
from rest_framework import serailizers
from apps.news.models import (
    Category, CategoryFile, SubCategory, SubCategoryFile,
)


class CategoryFileSerializer(ModelSerializer):
    class Meta:
        model = CategoryFile
        fields = ('id', 'image', 'category')
    

class CategorySerializer(ModelSerializer):
    files = CategoryFileSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'title', 'description', 'date', 'files')



class SubCategoryFileSerializer(ModelSerializer):
    class Meta:
        model = SubCategoryFile
        fields = ('id', 'image', 'subcategory')
    

class SubCategorySerializer(ModelSerializer):
    files = SubCategoryFileSerializer(read_only=True, many=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'title', 'description', 'date', 'files')