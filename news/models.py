from django.db import models
from django.contrib.auth.models import User

# il giornalista è chiave esterna in articoli
class Giornalista(models.Model):
    nome = models.TextField()
    cognome = models.TextField()

class Articoli(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name='articoli')
