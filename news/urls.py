from . import views
from .views import listaArticoliView,listaGiornalistiView#,listaArticoliGiornalistaView
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('news/',include('news.urls', namespace="news")),
    path('lista-articoli/', listaArticoliView.as_view(), name='lista_articoli'),
    path('lista-giornalisti',  listaGiornalistiView.as_view(), name='lista_giornalisti'),
]