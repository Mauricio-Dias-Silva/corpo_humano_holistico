from django.db import models
from core.models import EntidadeHolisticaMixin

class Chakra(EntidadeHolisticaMixin):
    """Ex: Básico, Cardíaco, Coronário"""
    nome = models.CharField(max_length=100)
    nome_sancrito = models.CharField(max_length=100, blank=True)
    cor = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Meridiano(EntidadeHolisticaMixin):
    """Canais de energia da acupuntura"""
    nome = models.CharField(max_length=100)
    elemento = models.CharField(max_length=50) # Fogo, Terra, etc.

    def __str__(self):
        return self.nome
