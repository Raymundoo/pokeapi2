from django.shortcuts import render, get_object_or_404
from pokemon.pokemon_api import Pokemon

# Create your views here.
#Test
def inicio(request):
    url = request.GET.get("url")
    if url:
        pokemones = Pokemon(url)
    else:
        pokemones = Pokemon("https://pokeapi.co/api/v2/pokemon/?limit=10", "general")
    pokemones = pokemones.obtener()
    return render(request, 'index.html', {"pokemones":pokemones})


def ver_pokemon(request, id_pokemon):
    caracteristicas = Pokemon.caracteristicas(id_pokemon)
    return render(request, 'ver_pokemon.html', {"pokemon": caracteristicas})

