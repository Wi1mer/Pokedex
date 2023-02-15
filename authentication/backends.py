from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
import requests, json


UserModel = get_user_model()
URL = 'https://pokeapi.co/api/v2/pokemon'

#  Permite loguearnos con el email o el nombre de usuario
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

# styles

#  Crea el fondo dinamico de sus atributos segun los mismos
def power_color(attributes: int):
    attributes = int(attributes)

    if attributes >= 0 and attributes < 15:
        return "color-scale-0"
    elif attributes >= 15 and attributes < 30:
        return "color-scale-1"
    elif attributes >= 30 and attributes < 45:
        return "color-scale-2"
    elif attributes >= 45 and attributes < 60:
        return "color-scale-3"
    elif attributes >= 60 and attributes < 75:
        return "color-scale-4"
    elif attributes >= 75 and attributes < 90:
        return "color-scale-5"
    elif attributes >= 90 and attributes < 105:
        return "color-scale-6"
    elif attributes >= 105 and attributes < 120:
        return "color-scale-7"
    elif attributes >= 120 and attributes < 135:
        return "color-scale-8"
    elif attributes >= 135 and attributes < 150:
        return "color-scale-9"
    elif attributes >= 150 and attributes <= 255:
        return "gradient-color"
    else:
        return " "

#  Crea el borde dinamico segun su media de poder
def border_colors(average):
    if average < 40:
        return ['#f00000', '#f12000', '#f20000']
    elif average >= 40 and average < 70:
        return ['#fa5000', '#fb6500', '#fc7000']
    elif average >= 40 and average < 70:
        return ['#0af000', '#0cf500', '#0ff000']    
    elif average >= 40 and average < 70:
        return ['#5ddcff', '#ffd700', '#43f000']
    else:
        return ['#ffd700', '#ff0000', '#fa6500']

#  Peticion para obtener la info de un pokemon
def get_pokemon(id_pokemon=''):
    response = requests.request("GET", URL+id_pokemon)
    data = json.loads(response.text)

    pokemon_info = {}
    pokemon_info["id"] = data["id"]
    pokemon_info['name'] = data["name"]
    pokemon_info['height'] = round(data['height']*0.1, 2)
    pokemon_info["weight"] = round(data["weight"]*0.1, 2)
    pokemon_info["order"] = data["order"]
    pokemon_info["base_experience"] = data["base_experience"] if data["base_experience"] != None else '???'
    pokemon_info["img"] = data["sprites"]["other"]["official-artwork"]["front_default"]
    pokemon_info["img2"] = data["sprites"]["other"]["official-artwork"]["front_shiny"]
    pokemon_info["hp"] = data["stats"][0]["base_stat"]
    pokemon_info["bg_hp"] = power_color(data["stats"][0]["base_stat"])
    pokemon_info["attack"] = data["stats"][1]["base_stat"]
    pokemon_info["bg_attack"] = power_color(data["stats"][1]["base_stat"])
    pokemon_info["defense"] = data["stats"][2]["base_stat"]
    pokemon_info["bg_defense"] = power_color(data["stats"][2]["base_stat"])
    pokemon_info["special_attack"] = data["stats"][3]["base_stat"]
    pokemon_info["bg_special_attack"] = power_color(data["stats"][3]["base_stat"])
    pokemon_info["special_defense"] = data["stats"][4]["base_stat"]
    pokemon_info["bg_special_defense"] = power_color(data["stats"][4]["base_stat"])
    pokemon_info["speed"] = data["stats"][5]["base_stat"]
    pokemon_info["bg_speed"] = power_color(data["stats"][5]["base_stat"])
    pokemon_info["types"] = data["types"]
    pokemon_info["total"] = (pokemon_info["hp"]+pokemon_info["attack"]+pokemon_info["defense"]+pokemon_info["special_attack"]+pokemon_info["special_defense"]+pokemon_info["speed"])
    pokemon_info["average"] = (pokemon_info["total"])/6
    pokemon_info["bg_average"] = power_color(pokemon_info["average"])
    pokemon_info["border_average"] = border_colors(pokemon_info["average"])
    
    return pokemon_info

# Peticion para obtener todos los pokemones
def get_pokemons(querystring=''):
    
    try:
        response = requests.request("GET", URL, params=querystring)
        data = json.loads(response.text)

    except requests.exceptions.RequestException as e:
        print(e)
        data = {}
        # exit()
    return data
