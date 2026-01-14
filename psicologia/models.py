from django.db import models
from core.models import EntidadeHolisticaMixin

class Emocao(EntidadeHolisticaMixin):
    """Ex: Raiva, Medo, Alegria, Gratidão"""
    nome = models.CharField(max_length=100)
    polaridade = models.CharField(max_length=20, choices=[('POSITIVA', 'Positiva'), ('NEGATIVA', 'Negativa'), ('NEUTRA', 'Neutra')])
    impacto_imediato = models.TextField(help_text="O que sente no corpo na hora?")

    def __str__(self):
        return self.nome

class Pensamento(EntidadeHolisticaMixin):
    """NEW: Padrões de pensamentos repetitivos. Ex: 'Sou uma vítima', 'O dinheiro é sujo'"""
    padrao = models.CharField(max_length=200, verbose_name="Padrão de Pensamento")
    categoria = models.CharField(max_length=50, choices=[('CRENCA_LIMITANTE', 'Crença Limitante'), ('AFIRMACAO', 'Afirmação Positiva'), ('RUMINACAO', 'Ruminação/Obsessão')])
    frequencia_estimada = models.CharField(max_length=100, help_text="Quantas vezes por dia isso ocorre em média na pessoa afetada", blank=True)

    def __str__(self):
        return self.padrao

class Arquetipo(EntidadeHolisticaMixin):
    """Ex: O Guerreiro, A Mãe, O Sabio (Jung etc)"""
    nome = models.CharField(max_length=100)
    sombra = models.TextField(help_text="O lado negativo deste arquétipo")
    luz = models.TextField(help_text="O lado positivo deste arquétipo")

    def __str__(self):
        return self.nome

class EstadoMental(EntidadeHolisticaMixin):
    """Ex: Estresse Crônico, Ansiedade, Flow, Meditação"""
    nome = models.CharField(max_length=100)
    ondas_cerebrais = models.CharField(max_length=50, help_text="Alfa, Beta, Theta, Delta, Gama")

    def __str__(self):
        return self.nome
