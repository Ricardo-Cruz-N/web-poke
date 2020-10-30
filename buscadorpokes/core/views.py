from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
import requests
from .forms import SubmitPoke
from json.decoder import JSONDecodeError

class HomePageView(TemplateView):
    template_name = "core/home.html"

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

def search(request):
    poke = {}
    if 'pokename' in request.GET:
        pokename = request.GET['pokename']
        url = 'https://pokeapi.co/api/v2/pokemon/' + pokename
        try:
            response = requests.get(url)
            poke = response.json()
        except JSONDecodeError as e:
            print("Error al buscar", e)
    return render(request, 'core/search.html', {'poke': poke})