from django.db import models
from core.models import EntidadeHolisticaMixin

class Substancia(EntidadeHolisticaMixin):
    """Ex: Cortisol, Adrenalina, Cafeína, Vitamina C"""
    TIPO_SUBSTANCIA = [
        ('HORMONIO', 'Hormônio'),
        ('NEUROTRANSMISSOR', 'Neurotransmissor'),
        ('NUTRIENTE', 'Nutriente/Vitamina'),
        ('MINERAL', 'Mineral'), # Added Mineral
        ('TOXINA', 'Toxina'),
        ('MEDICAMENTO', 'Medicamento'),
        ('DROGA', 'Droga Recreativa'),
        ('FITOQUIMICO', 'Fitoquímico (Plantas)'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_SUBSTANCIA)
    formula_quimica = models.CharField(max_length=50, blank=True)
    meia_vida = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

class Desequilibrio(models.Model):
    """
    NEW: Mapeia o que acontece na Falta ou no Excesso.
    Ex: Ferro -> Deficiência -> Anemia / Excesso -> Hemocromatose
    """
    substancia = models.ForeignKey(Substancia, on_delete=models.CASCADE, related_name='desequilibrios')
    tipo = models.CharField(max_length=20, choices=[('FALTA', 'Falta/Deficiência'), ('EXCESSO', 'Excesso/Toxicidade')])
    nome_condicao = models.CharField(max_length=100, blank=True, help_text="Nome médico da condição (Ex: Anemia)")
    sintomas = models.TextField(help_text="Lista de sintomas separados por vírgula")
    consequencias_holisticas = models.TextField(help_text="Impacto na mente e energia", blank=True)

    def __str__(self):
        return f"{self.tipo} de {self.substancia.nome}"

class Alimento(EntidadeHolisticaMixin):
    """Ex: Café, Carne Vermelha, Brócolis, Açúcar Refinado"""
    GRUPO_ALIMENTAR = [
        ('CARBOIDRATO', 'Carboidrato'),
        ('PROTEINA_ANIMAL', 'Proteína Animal'),
        ('PROTEINA_VEGETAL', 'Proteína Vegetal'),
        ('GORDURA', 'Gordura/Óleo'),
        ('FRUTA', 'Fruta'),
        ('VEGETAL', 'Vegetal/Legume'),
        ('BEBIDA', 'Bebida'),
        ('PROCESSADO', 'Alimento Processado'),
    ]
    NATUREZA_MTC = [
        ('QUENTE', 'Quente (Yang)'),
        ('MORNO', 'Morno'),
        ('NEUTRO', 'Neutro'),
        ('FRESCO', 'Fresco'),
        ('FRIO', 'Frio (Yin)'),
    ]
    
    nome = models.CharField(max_length=100)
    grupo = models.CharField(max_length=50, choices=GRUPO_ALIMENTAR)
    natureza_energetica = models.CharField(max_length=50, choices=NATUREZA_MTC, default='NEUTRO', help_text="Impacto térmico na MTC")
    compostos_ativos = models.ManyToManyField(Substancia, related_name='encontrado_em', blank=True)
    dosha_predominante = models.CharField(max_length=50, blank=True, help_text="Vata, Pitta, Kapha (Aumenta/Diminui)")

    def __str__(self):
        return self.nome

class ProcessoMetabolico(EntidadeHolisticaMixin):
    """Ex: Digestão, Ciclo de Krebs, Resposta Inflamatória, Metilação"""
    nome = models.CharField(max_length=100)
    orgaos_envolvidos = models.ManyToManyField('anatomia.Orgao', blank=True)
    descricao_tecnica = models.TextField(blank=True)

    def __str__(self):
        return self.nome
