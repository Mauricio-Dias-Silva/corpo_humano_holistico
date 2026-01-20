from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from anatomia.models import Orgao, SistemaCorporal
from psicologia.models import Emocao
from simbologia.models import Chakra, Meridiano
from core.models import RelacaoHolistica

class Command(BaseCommand):
    help = 'Popula o sistema com conhecimento Holístico Rico (MTC + Anatomia)'

    def handle(self, *args, **kwargs):
        self.stdout.write("🧠 Iniciando infusão de conhecimento...")

        # 1. Cria Sistemas e Órgãos (Anatomia)
        # Ajuste: Sistema -> SistemaCorporal
        sis_digestivo, _ = SistemaCorporal.objects.get_or_create(nome="Sistema Digestivo", defaults={'funcao_principal': 'Digestão'})
        sis_cardio, _ = SistemaCorporal.objects.get_or_create(nome="Sistema Cardiovascular", defaults={'funcao_principal': 'Circulação'})
        
        figado, _ = Orgao.objects.get_or_create(nome="Fígado", sistema=sis_digestivo, defaults={'funcao_biologica': 'Metabolismo'})
        coracao, _ = Orgao.objects.get_or_create(nome="Coração", sistema=sis_cardio, defaults={'funcao_biologica': 'Bombeamento'})
        estomago, _ = Orgao.objects.get_or_create(nome="Estômago", sistema=sis_digestivo, defaults={'funcao_biologica': 'Digestão Mecânica'})
        rins, _ = Orgao.objects.get_or_create(nome="Rins", sistema=sis_digestivo, defaults={'funcao_biologica': 'Filtragem'}) # Simplificação
        
        # 2. Cria Emoções (Psicologia)
        raiva, _ = Emocao.objects.get_or_create(nome="Raiva", polaridade="NEGATIVA")
        medo, _ = Emocao.objects.get_or_create(nome="Medo", polaridade="NEGATIVA")
        ansiedade, _ = Emocao.objects.get_or_create(nome="Ansiedade/Preocupação", polaridade="NEGATIVA")
        alegria, _ = Emocao.objects.get_or_create(nome="Alegria Excessiva", polaridade="NEUTRA")

        # 3. Cria Simbologia (Chakras/Meridianos)
        plexo_solar, _ = Chakra.objects.get_or_create(nome="Plexo Solar (Manipura)", defaults={'cor': "Amarelo", 'localizacao': "Acima do umbigo"})
        
        # Ajuste: Elemento não é model, usando Meridiano
        meridiano_figado, _ = Meridiano.objects.get_or_create(nome="Meridiano do Fígado", defaults={'elemento': "Madeira"})

        # 4. O GRANDE MOMENTO: RELAÇÕES (O Grafo Holístico)
        # Medicina Tradicional Chinesa (MTC)
        
        self.criar_relacao(raiva, figado, "AGRAVA", "Na MTC, a Raiva estagna o Qi do Fígado, causando irritabilidade e enxaqueca.", 9)
        self.criar_relacao(medo, rins, "INIBE", "O Medo consome a Essência (Jing) dos Rins, afetando vitalidade e ossos.", 8)
        self.criar_relacao(ansiedade, estomago, "AGRAVA", "Preocupação excessiva ataca o Baço/Estômago, prejudicando a digestão.", 7)
        
        # Relações Simbólicas
        self.criar_relacao(plexo_solar, estomago, "CORRELACAO", "O Chakra do Plexo Solar rege a digestão física e emocional.", 10)
        self.criar_relacao(meridiano_figado, figado, "SIMBOLIZA", "O Fígado é o órgão Yin do elemento Madeira.", 10)

        self.stdout.write(self.style.SUCCESS("✨ Conhecimento Integrado com Sucesso! O Grafo está vivo."))

    def criar_relacao(self, origem, destino, tipo, desc, forca):
        # Helper para criar GenericForeignKey
        ct_origem = ContentType.objects.get_for_model(origem)
        ct_destino = ContentType.objects.get_for_model(destino)
        
        RelacaoHolistica.objects.get_or_create(
            origem_content_type=ct_origem,
            origem_object_id=origem.id,
            destino_content_type=ct_destino,
            destino_object_id=destino.id,
            defaults={
                'tipo': tipo,
                'descricao': desc,
                'forca': forca,
                'fonte': 'Medicina Tradicional Chinesa (Seed)'
            }
        )
