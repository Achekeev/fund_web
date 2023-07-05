from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=70)
    title = models.CharField(verbose_name='title', max_length=70)
    description = models.TextField(verbose_name='description')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name    


class CategoryFile(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='files')
    image = models.FileField(verbose_name='files')

    def __str__(self) -> str:
        return self.category.name
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    name = models.CharField(verbose_name='name', max_length=70)
    title = models.CharField(verbose_name='title', max_length=70)
    description = models.TextField(verbose_name='description')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name    


class SubCategoryFile(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='files')
    image = models.FileField(verbose_name='files')

    def __str__(self) -> str:
        return self.subcategory.name