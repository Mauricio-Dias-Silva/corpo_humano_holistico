from django.contrib import admin
from .models import Paciente, Checkup

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo_biologico', 'dosha_ayurveda', 'tipo_sanguineo')
    search_fields = ('nome',)

@admin.register(Checkup)
class CheckupAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data', 'queixa_principal')
    list_filter = ('data', 'paciente')
    readonly_fields = ('diagnostico_ia',) # Protege o parecer da IA
