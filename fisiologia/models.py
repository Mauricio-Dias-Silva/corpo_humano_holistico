# fisiologia/models.py
from django.db import models
from anatomia.models import Orgao

TIPO_PARAM = [('FUNC','Funcional'),('ESTR','Estrutural')]
TIPO_EFEITO = [
    ('ESTIMULA','Estimula'),
    ('INIBE','Inibe'),
    ('PROTEGE','Protege'),
    ('LESIONA','Lesiona'),
    ('MODULA','Modula')
]

class ParametroFisiologico(models.Model):
    nome = models.CharField(max_length=120)
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, related_name='parametros')
    tipo = models.CharField(max_length=5, choices=TIPO_PARAM, default='FUNC')
    unidade = models.CharField(max_length=20, blank=True, null=True)
    referencia_min = models.FloatField(blank=True, null=True)
    referencia_max = models.FloatField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('nome', 'orgao')

    def __str__(self):
        return f"{self.nome} ({self.orgao.nome})"
