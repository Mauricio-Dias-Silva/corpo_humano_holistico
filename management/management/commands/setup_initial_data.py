# management/management/commands/setup_initial_data.py
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Cria os dados iniciais necessários para o projeto, como o Site padrão.'

    def handle(self, *args, **options):
        if not Site.objects.filter(pk=1).exists():
            Site.objects.create(pk=1, domain='example.com', name='example.com')
            self.stdout.write(self.style.SUCCESS('Site padrão com ID=1 foi criado com sucesso.'))
        else:
            self.stdout.write(self.style.WARNING('Site padrão com ID=1 já existe.'))