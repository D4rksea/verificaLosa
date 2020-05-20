from django.shortcuts import render
# from django.views.generic.list import listView
from django.views.generic.detail import DetailView
from .models import Articoli, Giornalista

def home(request):
    blog_command = ['lista articoli','lista giornalisti']
    context = {
        'menu': blog_command,
    }
    return render(request, "/index.html", context)

def index(request):
    blog_command = ['lista articoli','lista giornalisti']
    context = {
        'blog_command': blog_command,
    }
    return render(request, "verificaLosa/index.html", context)

class PostDetailView(listView):
    model = Articoli #modello dei dati da utilizzare
    template_name = "templates/news/articoli.html" #pagina per mostrare i dati

class PostDetailView2(listView):
    model = Giornalista #modello dei dati da utilizzare
    template_name = "templates/news/articoli.html" #pagina per mostrare i dati