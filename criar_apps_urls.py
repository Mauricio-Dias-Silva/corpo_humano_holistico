import os

# --- CONFIGURAÇÃO ---
PROJECT_NAME = "corpo_humano_holistico"
APPS = [
    'anatomia',
    'sistema_osseo',
    'sistema_muscular',
    'sistema_nervoso',
    'sistema_cardiovascular',
    'sistema_respiratorio',
    'sistema_digestivo',
    'sistema_urinario',
    'sistema_endocrino',
    'sistema_tegumentar',
    'sistema_reprodutor',
    'sistema_hematopoietico',
    'metabolismo',
    'psicologia',
    'simbologia',
    'usuarios',
]
BASE_TEMPLATE_DIR = 'templates'

# --- FUNÇÕES ---
def criar_views(app):
    views_content = f"""from django.shortcuts import render

def dashboard(request):
    return render(request, '{app}/dashboard.html')
"""
    views_path = os.path.join(app, 'views.py')
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(views_content)
    print(f"[OK] views.py criado para {app}")

def criar_urls(app):
    urls_content = f"""from django.urls import path
from . import views

app_name = '{app}'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
"""
    urls_path = os.path.join(app, 'urls.py')
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(urls_content)
    print(f"[OK] urls.py criado para {app}")

def criar_template(app):
    template_dir = os.path.join(BASE_TEMPLATE_DIR, app)
    os.makedirs(template_dir, exist_ok=True)
    template_path = os.path.join(template_dir, 'dashboard.html')
    template_content = f"""{{% extends 'base.html' %}}

{{% block title %}}{app.replace('_', ' ').title()}{{% endblock %}}

{{% block content %}}
<h2>{app.replace('_', ' ').title()} - Dashboard</h2>
<p>Bem-vindo à visualização do {app.replace('_', ' ').title()}.</p>
{{% endblock %}}
"""
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(template_content)
    print(f"[OK] template dashboard.html criado para {app}")

def atualizar_urls_principal():
    urls_path = os.path.join(PROJECT_NAME, 'urls.py')
    
    include_lines = ""
    for app in APPS:
        if app != 'usuarios':  # se quiser manter usuarios separado pode customizar
            include_lines += f"    path('{app}/', include('{app}.urls')),\n"

    urls_content = f"""from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
{include_lines}]
"""
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(urls_content)
    print("[OK] urls.py principal atualizado com todos os apps")

# --- EXECUÇÃO ---
for app in APPS:
    criar_views(app)
    criar_urls(app)
    criar_template(app)

atualizar_urls_principal()

print("\n✅ Todos os arquivos e urls.py principal foram criados com sucesso!")
