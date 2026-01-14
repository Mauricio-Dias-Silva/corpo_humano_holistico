from django.db import models
from django.utils import timezone
from core.models import EntidadeHolisticaMixin

class Paciente(EntidadeHolisticaMixin):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo_biologico = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M')
    
    # Perfil Holístico
    dosha_ayurveda = models.CharField(max_length=50, blank=True, help_text="Vata, Pitta, Kapha")
    tipo_sanguineo = models.CharField(max_length=5, blank=True)
    
    def __str__(self):
        return self.nome

class Checkup(models.Model):
    """
    Um retrato da saúde do paciente em um momento do tempo.
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='checkups')
    data = models.DateTimeField(default=timezone.now)
    
    # Sintomas Relatados (Texto livre ou Tags)
    queixa_principal = models.TextField()
    sintomas_emocionais = models.TextField(blank=True, help_text="Tristeza, ansiedade, raiva...")
    
    # Diagnóstico da IA
    diagnostico_ia = models.TextField(blank=True, verbose_name="Parecer do Oráculo")
    
    def __str__(self):
        return f"Checkup de {self.paciente.nome} em {self.data.strftime('%d/%m/%Y')}"
