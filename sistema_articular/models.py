from django.db import models
from anatomia.models import Orgao

class Estrutura(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da articulação, ex: 'Joelho', 'Ombro'")
    orgao_relacionado = models.ForeignKey(Orgao, on_delete=models.SET_NULL, null=True, blank=True)
    funcao = models.TextField(blank=True, null=True, help_text="Função da articulação (movimento, estabilidade)")
    
    def __str__(self):
        return self.nome
