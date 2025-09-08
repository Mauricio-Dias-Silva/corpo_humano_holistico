# anatomia/models.py
from django.db import models

class Orgao(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
