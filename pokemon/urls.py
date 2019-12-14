from django.conf.urls import include, url
from pokemon.views import inicio, ver_pokemon

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^ver-pokemon/(?P<id_pokemon>[\w.@+-]+)/$', ver_pokemon, name='ver_pokemon'),
]