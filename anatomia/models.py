from django.db import models
from core.models import EntidadeHolisticaMixin

class SistemaCorporal(EntidadeHolisticaMixin):
    """Ex: Sistema Nervoso, Digestivo, Endócrino"""
    nome = models.CharField(max_length=100)
    funcao_principal = models.TextField()
    cor_associada = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

class Orgao(EntidadeHolisticaMixin):
    """Ex: Coração, Fígado, Pineal"""
    nome = models.CharField(max_length=100)
    sistema = models.ForeignKey(SistemaCorporal, on_delete=models.CASCADE, related_name='orgaos')
    funcao_biologica = models.TextField()
    
    # --- KENHUB / ATLAS LEVEL DATA ---
    origem = models.CharField(max_length=200, blank=True, help_text="Ex: Clavícula (Anatomia Muscular)")
    insercao = models.CharField(max_length=200, blank=True, help_text="Ex: Úmero")
    inervacao = models.CharField(max_length=200, blank=True, help_text="Ex: Nervo Axilar")
    vascularizacao = models.CharField(max_length=200, blank=True, help_text="Ex: Artérias Circunflexas")
    
    # Medicina Tradicional Chinesa (MTC)
    elemento_mtc = models.CharField(max_length=50, choices=[('FOGO', 'Fogo'), ('TERRA', 'Terra'), ('METAL', 'Metal'), ('AGUA', 'Água'), ('MADEIRA', 'Madeira')], blank=True)
    horario_pico = models.CharField(max_length=50, help_text="Horário do relógio biológico", blank=True)
    representacao_emocional = models.CharField(max_length=200, help_text="Ex: O Fígado armazena a raiva", blank=True)

    def __str__(self):
        return self.nome

class Tecido(EntidadeHolisticaMixin):
    """Ex: Sangue, Osso, Pele"""
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100) # Epitelial, Conjuntivo, etc.

    def __str__(self):
        return self.nome

# --- NEW: MICRO-BIOLOGIA ---
class Celula(EntidadeHolisticaMixin):
    """Ex: Neurônio, Hepatócito, Hemácia, Leucócito"""
    nome = models.CharField(max_length=100)
    tipo_geral = models.CharField(max_length=50) # Sanguínea, Nervosa, Muscular
    tempo_vida_medio = models.CharField(max_length=50, blank=True, help_text="Ex: 120 dias")
    funcao_micro = models.TextField(verbose_name="Função Celular")
    
    # Relação com órgãos (Muitas celulas compoem um orgao)
    encontrada_em = models.ManyToManyField(Orgao, blank=True, related_name='tipos_celulares')

    def __str__(self):
        return self.nome
