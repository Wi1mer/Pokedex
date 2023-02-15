from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, LoginForm
from .backends import get_pokemons, get_pokemon

# Create your views here.

def pokemons(request):
    data = get_pokemons({"limit":"100000","offset":"0"})

    if data:
        return render(request, "pokedex/templates/pokemons.html", {"pokemons":data['results']})
    else:
        return render(request, "pokedex/templates/pokemons.html")

def pokemon(request, id):
    data = get_pokemon(f"/{id}")

    if request.user.is_authenticated:
        return render(request, "pokedex/templates/pokemon.html", {"pokemon":data})
    else:
        return redirect('loguear')

def loguear(request):
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)

        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)

            if usuario is not None:
                login(request,usuario)
                return redirect('pokemons')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")

    form=LoginForm()
    return render(request,'pokedex/templates/login.html',{"form":form})


def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def back_page(request):
    return redirect(request.META.get('HTTP_REFERER', '/'))

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("loguear")
    template_name = "pokedex/templates/register.html"