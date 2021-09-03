from django.contrib import admin

from .models import Ingredient, Recipe, DishType

class IngredientInline(admin.TabularInline):
  model = Ingredient
  extra = 1

class RecipeAdmin(admin.ModelAdmin):
  inlines = [IngredientInline]
  model = Recipe

admin.site.register(DishType)
admin.site.register(Recipe, RecipeAdmin)