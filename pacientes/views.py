from django.shortcuts import render, redirect
from django.views import View
from .models import Paciente, Checkup
from core.brain import CérebroHolistico

class DiagnosticView(View):
    def get(self, request):
        return render(request, 'pacientes/diagnostico.html')

    def post(self, request):
        nome = request.POST.get('nome')
        queixa = request.POST.get('queixa')
        idade = request.POST.get('idade')
        
        # 1. Criar ou Atualizar Paciente (Simplificado)
        paciente, _ = Paciente.objects.get_or_create(nome=nome)
        
        # 2. Processar Diagnóstico
        brain = CérebroHolistico()
        laudo = brain.diagnosticar_holisticamente(queixa)
        
        # 3. Salvar Checkup
        Checkup.objects.create(
            paciente=paciente,
            queixa_principal=queixa,
            diagnostico_ia=laudo
        )
        
        return render(request, 'pacientes/diagnostico.html', {
            'laudo': laudo,
            'paciente': paciente,
            'queixa': queixa
        })
