from django.db import models
from autoslug import AutoSlugField

class DishType(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title