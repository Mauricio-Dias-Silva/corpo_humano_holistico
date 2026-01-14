from django.core.management.base import BaseCommand
from core.models import RelacaoHolistica
from anatomia.models import Orgao, SistemaCorporal, Celula
from psicologia.models import Emocao, Pensamento
from metabolismo.models import Substancia, Alimento, ProcessoMetabolico, Desequilibrio
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta o Conhecimento Universal Completo (Células, Deficiências, Bio-IA)'

    def handle(self, *args, **kwargs):
        self.stdout.write("🧬 Iniciando Mapeamento Celular e Bioquímico Profundo...")

        # --- 1. SUBSTÂNCIAS VITAIS & MINERAIS ---
        ferro, _ = Substancia.objects.get_or_create(nome='Ferro', defaults={'tipo': 'MINERAL'})
        magnesio, _ = Substancia.objects.get_or_create(nome='Magnésio', defaults={'tipo': 'MINERAL'})
        b12, _ = Substancia.objects.get_or_create(nome='Vitamina B12', defaults={'tipo': 'NUTRIENTE'})
        cortisol, _ = Substancia.objects.get_or_create(nome='Cortisol', defaults={'tipo': 'HORMONIO'})
        
        # --- 2. DESEQUILÍBRIOS (O que a falta ou excesso causa) ---
        Desequilibrio.objects.get_or_create(
            substancia=ferro, tipo='FALTA',
            defaults={
                'nome_condicao': 'Anemia Ferropriva', 
                'sintomas': 'Cansaço extremo, palidez, falta de ar, unhas quebradiças', 
                'consequencias_holisticas': 'Falta de força vital, incapacidade de se defender, fraqueza no "Eu Sou".'
            }
        )
        Desequilibrio.objects.get_or_create(
            substancia=magnesio, tipo='FALTA',
            defaults={
                'nome_condicao': 'Hipomagnesemia', 
                'sintomas': 'Cãibras, ansiedade, insônia, taquicardia', 
                'consequencias_holisticas': 'Tensão mental, incapacidade de relaxar e fluir com a vida.'
            }
        )
        Desequilibrio.objects.get_or_create(
            substancia=cortisol, tipo='EXCESSO',
            defaults={
                'nome_condicao': 'Estresse Crônico / Cushing', 
                'sintomas': 'Gordura abdominal, rosto inchado, pressão alta, ansiedade', 
                'consequencias_holisticas': 'Viver em modo de sobrevivência constante, medo do futuro.'
            }
        )

        # --- 3. MICRO-BIOLOGIA (Células) ---
        hemacia, _ = Celula.objects.get_or_create(
            nome='Hemácia (Glóbulo Vermelho)', 
            defaults={
                'tipo_geral': 'Sanguínea', 
                'tempo_vida_medio': '120 dias',
                'funcao_micro': 'Transporte de O2 e CO2 via Hemoglobina.'
            }
        )
        neuronio, _ = Celula.objects.get_or_create(
            nome='Neurônio Motor', 
            defaults={
                'tipo_geral': 'Nervosa', 
                'funcao_micro': 'Transmite impulsos elétricos para movimento.'
            }
        )
        osteoblasto, _ = Celula.objects.get_or_create(
            nome='Osteoblasto', 
            defaults={
                'tipo_geral': 'Óssea', 
                'funcao_micro': 'Constrói nova matriz óssea (renovação).'
            }
        )

        # --- 4. RELAÇÕES PROFUNDAS ---
        # Ferro compõe a Hemácia
        ct_ferro = ContentType.objects.get_for_model(ferro)
        ct_hemacia = ContentType.objects.get_for_model(hemacia)
        RelacaoHolistica.objects.get_or_create(
            origem_content_type=ct_ferro, origem_object_id=ferro.id,
            destino_content_type=ct_hemacia, destino_object_id=hemacia.id,
            tipo='ESTIMULA', # Na verdade compõe
            defaults={'descricao': 'O Ferro é o núcleo da Hemoglobina dentro da Hemácia.', 'forca': 10}
        )

        self.stdout.write(self.style.SUCCESS('✅ Mapeamento Profundo Concluído! O Cérebro está pronto para conversar.'))
