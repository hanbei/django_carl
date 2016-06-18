from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.random_recipe, name='random'),
    url(r'^recipes/$', views.index, name='index'),
    url(r'^recipes/(?P<recipe_id>[0-9]+)/$', views.details, name='details'),
]