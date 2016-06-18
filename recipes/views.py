import random

from django.shortcuts import render, get_object_or_404
from django.views import generic
from recipes.models import Recipe


def random_recipe(request):
    recipes = Recipe.objects.order_by('id')
    context = {'recipe': random.choice(recipes)}
    return render(request=request, template_name='recipes/random.html', context=context)


class ListView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.order_by('id')


# def index(request):
#     recipes = Recipe.objects.order_by('id')
#     print(recipes)
#     context = {'recipes': recipes,}
#     return render(request=request, template_name='recipes/index.html', context=context)

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/details.html'

# def details(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     return render(request=request, template_name='recipes/details.html', context={'recipe': recipe})
