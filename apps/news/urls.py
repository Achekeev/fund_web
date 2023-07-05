from rest_framework.routers import DefaultRouter as DR
from apps.news.views import (
    CategoryViewSet, SubCategoryViewSet, CategoryFileViewSet, SubCategoryFileViewSet
)



router = DR()

router.register('category', CategoryViewSet, basename='Category')
router.register('subcategory', SubCategoryViewSet, basename='SubCategory')
router.register('category_file', CategoryFileViewSet, basename='Category file')
router.register('subcategory_file', SubCategoryFileViewSet, basename='SubCategory file')


urlpatterns = []

urlpatterns += router.urls