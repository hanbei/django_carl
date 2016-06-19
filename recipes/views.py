import random

from django.shortcuts import render, get_object_or_404
from django.views import generic
from recipes.models import Recipe


def random_recipe(request):
    recipes = Recipe.objects.order_by('id')
    if recipes:
        context = {'recipe': random.choice(recipes)}
    else:
        context = {}
    return render(request=request, template_name='recipes/random.html', context=context)


class ListView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/details.html'

