from django.contrib import admin

from .models import Recipe, DishType

admin.site.register([Recipe, DishType])