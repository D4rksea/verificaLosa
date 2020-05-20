from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lista-articoli/', views.listaArt(), name='lista_articoli'),
]