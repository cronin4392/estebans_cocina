from django.shortcuts import get_object_or_404, render

from .models import Recipe

def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    context = {'recipe_list': recipe_list}
    return render(request, "website/index.html", context)

def recipe(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    return render(request, 'website/recipe/index.html', {'recipe': recipe})