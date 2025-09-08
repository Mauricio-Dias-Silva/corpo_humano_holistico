# core/views.py
from django.shortcuts import render
from .ai_service import get_aura_greeting
from usuarios.models import PerfilUsuario # Importando nosso model!

# core/views.py
# ... (imports no topo) ...

def homepage(request):
    context = {}

    # Estrutura de dados para o nosso Mega Menu
    mega_menu_sistemas = {
        "Estrutura e Movimento": [
            {'nome': 'Sistema Ósseo', 'app_name': 'sistema_osseo'},
            {'nome': 'Sistema Muscular', 'app_name': 'sistema_muscular'},
            {'nome': 'Sistema Tegumentar', 'app_name': 'sistema_tegumentar'},
        ],
        "Controle e Comunicação": [
            {'nome': 'Sistema Nervoso', 'app_name': 'sistema_nervoso'},
            {'nome': 'Sistema Endócrino', 'app_name': 'sistema_endocrino'},
        ],
        "Transporte e Defesa": [
            {'nome': 'Sistema Cardiovascular', 'app_name': 'sistema_cardiovascular'},
            {'nome': 'Sistema Circulatório', 'app_name': 'sistema_circulatorio'},
            {'nome': 'Sistema Respiratório', 'app_name': 'sistema_respiratorio'},
            {'nome': 'Sistema Imunológico', 'app_name': 'sistema_immune'},
            {'nome': 'Sistema Hematopoiético', 'app_name': 'sistema_hematopoietico'},
        ],
        "Processamento e Energia": [
            {'nome': 'Sistema Digestivo', 'app_name': 'sistema_digestivo'},
            {'nome': 'Sistema Urinário', 'app_name': 'sistema_urinario'},
            {'nome': 'Metabolismo', 'app_name': 'metabolismo'},
        ],
        "Mente e Simbologia": [
            {'nome': 'Psicologia', 'app_name': 'psicologia'},
            {'nome': 'Simbologia', 'app_name': 'simbologia'},
             {'nome': 'Sistema Reprodutor', 'app_name': 'sistema_reprodutor'}, # Exemplo
        ]
    }
    context['mega_menu_sistemas'] = mega_menu_sistemas

    if request.user.is_authenticated:
        # ... (Lógica da Aura como antes) ...
        pass # Mantenha sua lógica da Aura aqui

    return render(request, 'home.html', context)