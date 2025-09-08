from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import IntegrityError

# Lista de apps do seu projeto (não inclui apps do Django)
MEUS_APPS = [
    'anatomia', 'sistema_osseo', 'sistema_muscular', 'sistema_nervoso',
    'sistema_cardiovascular', 'sistema_respiratorio', 'sistema_digestivo',
    'sistema_urinario', 'sistema_endocrino', 'sistema_tegumentar',
    'sistema_reprodutor', 'sistema_hematopoietico', 'sistema_circulatorio',
    'sistema_immune', 'metabolismo', 'psicologia', 'simbologia', 'usuarios', 'core'
]

class Command(BaseCommand):
    help = "Popula todos os apps com Estruturas ou dados dummy para visualização"

    def handle(self, *args, **options):
        self.stdout.write("🚀 Populando todos os apps do sistema...")

        for app_label in MEUS_APPS:
            try:
                Estrutura = apps.get_model(app_label, 'Estrutura')
                # Criar 5 estruturas de teste para cada app
                for i in range(1, 6):
                    try:
                        Estrutura.objects.create(
                            nome=f"{app_label}_estrutura_{i}",
                            orgao_relacionado=None  # pode ajustar para órgãos reais
                        )
                    except IntegrityError:
                        continue
                self.stdout.write(f"[OK] Estruturas criadas para {app_label}")

            except LookupError:
                # Modelo Estrutura não existe -> criar dummy para visualização
                dummy_data = [
                    {"nome": f"{app_label}_dummy_{i}"} for i in range(1, 6)
                ]
                self.stdout.write(f"⚠ {app_label}: Modelo Estrutura não encontrado. Criando dummy para visualização:")
                for d in dummy_data:
                    self.stdout.write(f"    {d['nome']}")

        self.stdout.write("✅ População de dados finalizada!")

