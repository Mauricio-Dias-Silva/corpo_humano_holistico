import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
APPS = [
    "anatomia", "sistema_osseo", "sistema_muscular", "sistema_nervoso",
    "sistema_cardiovascular", "sistema_respiratorio", "sistema_digestivo",
    "sistema_urinario", "sistema_endocrino", "sistema_tegumentar",
    "sistema_reprodutor", "sistema_hematopoietico", "sistema_circulatorio",
    "sistema_immune", "metabolismo", "psicologia", "simbologia", "usuarios", "core"
]

# 1️⃣ Cria views básicas para cada app
for app in APPS:
    views_path = BASE_DIR / app / "views.py"
    if not views_path.exists():
        with open(views_path, "w", encoding="utf-8") as f:
            f.write(f"""from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request, '{app}/dashboard.html')
""")
        print(f"[OK] views.py criado para {app}")

# 2️⃣ Cria templates de dashboard com links para outros sistemas
for app in APPS:
    templates_dir = BASE_DIR / app / "templates" / app
    os.makedirs(templates_dir, exist_ok=True)
    dashboard_path = templates_dir / "dashboard.html"
    with open(dashboard_path, "w", encoding="utf-8") as f:
        links = "".join([f'<li><a href="/{other}/">{other}</a></li>' for other in APPS if other != app])
        f.write(f"""{{% extends "base.html" %}}

{{% block content %}}
<h1>Dashboard {app}</h1>
<p>Visualize estruturas e órgãos:</p>
<ul>
{links}
</ul>
{{% endblock %}}
""")
        print(f"[OK] dashboard.html criado para {app}")

# 3️⃣ Popula banco com seed inicial para cada app
seed_path = BASE_DIR / "seed_data.py"
with open(seed_path, "w", encoding="utf-8") as f:
    f.write("""from django.core.management.base import BaseCommand
from anatomia.models import Orgao
from sistema_osseo.models import Estrutura

class Command(BaseCommand):
    help = 'Popula dados iniciais do sistema'

    def handle(self, *args, **kwargs):
        # Exemplo: órgãos
        orgaos = ['Coração', 'Fígado', 'Rim', 'Pulmão', 'Estômago']
        for nome in orgaos:
            Orgao.objects.get_or_create(nome=nome)
        self.stdout.write(self.style.SUCCESS('Orgaos criados com sucesso!'))

        # Exemplo: estruturas ósseas
        from sistema_osseo.models import Estrutura
        Estrutura.objects.get_or_create(nome='Fêmur', orgao_relacionado=Orgao.objects.first())
        Estrutura.objects.get_or_create(nome='Tíbia', orgao_relacionado=Orgao.objects.last())
        self.stdout.write(self.style.SUCCESS('Estruturas criadas com sucesso!'))
""")
print("[OK] seed_data.py criado para popular o banco")

print("✅ Views, dashboards e seed criados. Agora rode:")
print("  python manage.py makemigrations")
print("  python manage.py migrate")
print("  python manage.py loaddata seed_data.py  # depois vamos transformar em comando custom")
