import os

# Lista de apps e o related_name que cada um vai usar
apps = {
    "anatomia": None,  # não precisa de related_name porque é o Orgao principal
    "sistema_osseo": "estrutura_osseo",
    "sistema_muscular": "estrutura_muscular",
    "sistema_nervoso": "estrutura_nervoso",
    "sistema_cardiovascular": "estrutura_cardiovascular",
    "sistema_respiratorio": "estrutura_respiratorio",
    "sistema_digestivo": "estrutura_digestivo",
    "sistema_urinario": "estrutura_urinario",
    "sistema_endocrino": "estrutura_endocrino",
    "sistema_tegumentar": "estrutura_tegumentar",
    "sistema_reprodutor": "estrutura_reprodutor",
    "sistema_hematopoietico": "estrutura_hematopoietico",
    "sistema_circulatorio": "estrutura_circulatorio",
    "sistema_immune": "estrutura_immune",
    "metabolismo": None,
    "psicologia": None,
    "simbologia": None,
    "usuarios": None,
    "core": None
}

for app, related_name in apps.items():
    models_path = os.path.join(app, "models.py")
    os.makedirs(app, exist_ok=True)

    # Define o conteúdo base
    content = "from django.db import models\n"
    
    if app != "anatomia" and related_name:
        content += "from anatomia.models import Orgao\n\n"
        content += f"class Estrutura(models.Model):\n"
        content += "    nome = models.CharField(max_length=100)\n"
        content += f"    orgao_relacionado = models.ForeignKey(Orgao, on_delete=models.SET_NULL, null=True, blank=True, related_name='{related_name}')\n"
        content += "    funcao = models.TextField(blank=True, null=True)\n\n"
        content += "    def __str__(self):\n"
        content += "        return self.nome\n"
    else:
        # Model vazio para apps que não usam Estrutura
        content += f"# Models para {app}\n"

    with open(models_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"[OK] models.py criado para {app}")

# No final, avisa sobre o próximo passo
print("\n✅ Todos os models.py foram criados com related_name correto!")
print("Rode agora:\n python manage.py makemigrations\n python manage.py migrate")
