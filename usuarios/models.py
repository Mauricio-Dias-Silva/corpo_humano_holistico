# usuarios/models.py
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    ATIVIDADE_CHOICES = [
        (1.2, 'Sedentário'),
        (1.375, 'Levemente Ativo'),
        (1.55, 'Moderadamente Ativo'),
        (1.725, 'Muito Ativo'),
        (1.9, 'Extremamente Ativo'),
    ]
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    peso_kg = models.FloatField(null=True, blank=True)
    altura_cm = models.FloatField(null=True, blank=True)
    nivel_atividade = models.FloatField(choices=ATIVIDADE_CHOICES, default=1.2)

    def __str__(self):
        return f"Perfil de {self.user.username}"