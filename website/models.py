from django.db import models
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError

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

class Ingredient(models.Model):
    class Unit(models.TextChoices):
        TBSP = 'TBSP', 'tbsp.'
        TSP = 'TSP', 'tsp.'
        OZ = 'OZ', 'oz'
        LB = 'LB', 'lb'
        CUP = 'CUP', 'cup'
        BUNCH = 'BUNCH', 'bunch'

    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=5, choices=Unit.choices, null=True, blank=True)
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def clean(self):
        if self.unit and not self.amount:
            raise ValidationError(
                "You must provide a unit if there is an amount"
            )

    def __str__(self):
        return self.name