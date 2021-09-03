from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<slug:recipe_slug>/', views.recipe, name='recipe'),
]