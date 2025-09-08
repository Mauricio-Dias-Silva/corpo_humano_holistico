from django.db import models
from anatomia.models import Orgao

class Estrutura(models.Model):
    nome = models.CharField(max_length=100)
    orgao_relacionado = models.ForeignKey(Orgao, on_delete=models.SET_NULL, null=True, blank=True, related_name='estrutura_tegumentar')
    funcao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
