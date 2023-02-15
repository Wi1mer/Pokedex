from django.urls import path
from . import views
from .views import loguear, cerrar_sesion, SignUpView


urlpatterns = [
    # path('', views.home, name='home'),
    path('pokemon/<int:id>', views.pokemon, name='pokemon'),
    path('pokemons/', views.pokemons, name='pokemons'),
    path('pokemons/', views.back_page, name='back_page'),

    path('loguear/', loguear, name='loguear'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path("registro/", SignUpView.as_view(), name="registro"),
]