from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import uuid

class EntidadeHolisticaMixin(models.Model):
    """
    Mixin base para todas as entidades do sistema (Orgãos, Emoções, Chakras, etc).
    Permite que qualquer coisa se conecte com qualquer coisa.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao_detalhada = models.TextField(blank=True, verbose_name="Descrição Detalhada")
    frequencia_hz = models.FloatField(default=0.0, verbose_name="Frequência Base (Hz)", help_text="Vibração energética aproximada")
    
    # Campo para conexões reversas genéricas
    # relacoes_origem = GenericRelation('RelacaoHolistica', content_type_field='origem_content_type', object_id_field='origem_object_id')
    # relacoes_destino = GenericRelation('RelacaoHolistica', content_type_field='destino_content_type', object_id_field='destino_object_id')

    class Meta:
        abstract = True

class RelacaoHolistica(models.Model):
    """
    O 'Nervo' do sistema. Conecta qualquer entidade A a qualquer entidade B.
    Ex: Medo (Psicologia) -> Rins (Anatomia) [Causa Desequilíbrio]
    """
    TIPO_RELACAO = [
        ('CAUSA_FISICA', 'Causa Física'),
        ('CAUSA_EMOCIONAL', 'Causa Emocional'),
        ('INIBE', 'Inibe/Bloqueia'),
        ('ESTIMULA', 'Estimula/Ativa'),
        ('SIMBOLIZA', 'Simboliza/Representa'),
        ('CURA', 'Cura/Trata'),
        ('AGRAVA', 'Agrava/Piora'),
        ('CORRELACAO', 'Correlação Direta'),
    ]

    # Origem da conexão
    origem_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='+')
    origem_object_id = models.UUIDField()
    origem = GenericForeignKey('origem_content_type', 'origem_object_id')

    # Destino da conexão
    destino_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='+')
    destino_object_id = models.UUIDField()
    destino = GenericForeignKey('destino_content_type', 'destino_object_id')

    tipo = models.CharField(max_length=50, choices=TIPO_RELACAO)
    descricao = models.TextField(help_text="Explicação científica ou esotérica da conexão")
    forca = models.IntegerField(default=5, help_text="Força da conexão de 1 a 10")
    
    # Fonte do conhecimento (Científico, Tradicional Chinesa, Ayurveda, etc)
    fonte = models.CharField(max_length=100, default="Medicina Integrativa")

    def __str__(self):
        return f"{self.origem} -> {self.tipo} -> {self.destino}"
