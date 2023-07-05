from django.contrib import admin
from apps.news.models import (
    Category, CategoryFile, SubCategory, SubCategoryFile
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CategoryFile)
admin.site.register(SubCategoryFile)