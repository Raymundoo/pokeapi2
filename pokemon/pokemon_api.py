# -*- coding: utf-8 -*-
import requests
from django.utils import formats
import json

class Pokemon:
    def __init__(self, endpoint, tipo=None):
        self.endpoint = endpoint
        self.tipo = tipo

    def obtener(self):
        url = self.endpoint
        response = requests.get(url)
        list_pokemones = []
        if response.status_code == 200:
            content = json.loads(response.content)
            if self.tipo == "general":
                results = content["results"]
                for pokemon in results:
                    nombre = pokemon.get("name")

                    url_propiedades_pokemon = pokemon.get("url")
                    response_propiedades_pokemon = requests.get(url_propiedades_pokemon)


                    if response_propiedades_pokemon.status_code == 200:
                        content_pokemon = json.loads(response_propiedades_pokemon.content)
                        imagen = content_pokemon.get("sprites")["back_default"]                   
                        id_pokemon = content_pokemon.get("id")
                    dicc_pokemon = {"nombre": nombre, "imagen": imagen, "id_pokemon": id_pokemon}
                    list_pokemones.append(dicc_pokemon)
            else:
                results = content["pokemon"]
                for pokemon in results:
                    nombre = pokemon.get("pokemon")["name"]

                    url_propiedades_pokemon = pokemon.get("pokemon")["url"]
                    response_propiedades_pokemon = requests.get(url_propiedades_pokemon)


                    if response_propiedades_pokemon.status_code == 200:
                        content_pokemon = json.loads(response_propiedades_pokemon.content)
                        imagen = content_pokemon.get("sprites")["back_default"]                   
                        id_pokemon = content_pokemon.get("id")
                    dicc_pokemon = {"nombre": nombre, "imagen": imagen, "id_pokemon": id_pokemon}
                    list_pokemones.append(dicc_pokemon)
        return list_pokemones

    @staticmethod
    def caracteristicas(id_pokemon):
        dicc_pokemon = ""
        url_pokemon = "https://pokeapi.co/api/v2/pokemon/{0}/".format(id_pokemon)
        response_pokemon = requests.get(url_pokemon)
        if response_pokemon.status_code == 200:
            content_pokemon = json.loads(response_pokemon.content)
            dicc_pokemon = {
                "nombre": content_pokemon.get("forms")[0]["name"],
                "imagen": content_pokemon.get("sprites")["back_default"],
                "altura": content_pokemon.get("height"),
                "peso": content_pokemon.get("weight"),
                "tipos": content_pokemon.get("types"),
                "habilidades": content_pokemon.get("abilities"),
                "movimientos": content_pokemon.get("moves")
            }
        return dicc_pokemon