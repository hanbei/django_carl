from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.random_recipe, name='random'),
    url(r'^recipes/$', views.ListView.as_view(), name='index'),
    url(r'^recipes/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
]
