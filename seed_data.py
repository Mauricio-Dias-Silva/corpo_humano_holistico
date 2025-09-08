from django.core.management.base import BaseCommand
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
