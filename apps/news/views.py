from rest_framework.viewsets import ModelViewSet
from apps.news.models import (
    Category, SubCategory, CategoryFile, SubCategoryFile
)
from apps.news.serializers import (
    CategorySerializer, CategoryFileSerializer, SubCategorySerializer, SubCategoryFileSerializer 
)






class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CategoryFileViewSet(ModelViewSet):
    queryset = CategoryFile.objects.all()
    serializer_class = CategoryFileSerializer


class SubCategoryFileViewSet(ModelViewSet):
    queryset = SubCategoryFile.objects.all()
    serializer_class = SubCategoryFileSerializer