from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Articoli, Giornalista

def home(request):
    return render(request, "home.html")

class GiornalistiView(listView):
    model = Giornalista #modello dei dati da utilizzare
    template_name = "templates/news/articoli.html" #pagina per mostrare i dati

class ArticoliView(listView):
    model = Articoli #modello dei dati da utilizzare
    template_name = "templates/news/articoli.html" #pagina per mostrare i dati