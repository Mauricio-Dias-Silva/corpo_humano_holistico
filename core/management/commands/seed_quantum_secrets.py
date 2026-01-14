from django.core.management.base import BaseCommand
from anatomia.models import Orgao, Celula, SistemaCorporal
from metabolismo.models import Substancia, ProcessoMetabolico, Desequilibrio
from psicologia.models import Pensamento, EstadoMental
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta Conhecimentos Raros (Biofísica Quântica, Esoterismo Científico).'

    def handle(self, *args, **kwargs):
        self.stdout.write("✨ Acessando Arquivos Akáshicos & Quânticos...")

        def conectar(origem, destino, tipo, desc, forca=10):
            if origem and destino:
                 RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca, 'fonte': 'Física Quântica / Misticismo'}
                )

        # === 1. BIOFÓTONS (A Luz do DNA) ===
        dna, _ = Celula.objects.get_or_create(nome='DNA (Material Genético)', defaults={'tipo_geral': 'Molecular', 'funcao_micro': 'Armazenamento de Informação'})
        biofotons, _ = Substancia.objects.get_or_create(nome='Biofótons', defaults={'tipo': 'NUTRIENTE', 'formula_quimica': 'Luz Coerente (hν)'})
        
        conectar(dna, biofotons, 'PRODUZ', 'Segundo F.A. Popp, o DNA armazena e emite luz coerente (Biofótons) para comunicar-se instantaneamente com todas as células.', 10)
        
        # === 2. CONSCIÊNCIA QUÂNTICA (Orch-OR) ===
        microtubulos, _ = Celula.objects.get_or_create(nome='Microtúbulos', defaults={'tipo_geral': 'Estrutura Celular', 'funcao_micro': 'Citoesqueleto e Transporte'})
        
        consciencia, _ = EstadoMental.objects.get_or_create(nome='Consciência Não-Local', defaults={'ondas_cerebrais': 'Gamma 40Hz+'})
        
        conectar(microtubulos, consciencia, 'PROCESSA', 'Teoria Penrose-Hameroff: Microtúbulos agem como computadores quânticos, colapsando a função de onda da realidade (Orch-OR).')
        
        # === 3. O CORAÇÃO TOROIDAL ===
        coracao = Orgao.objects.filter(nome__icontains='Coração').first()
        campo_eletromagnetico, _ = ProcessoMetabolico.objects.get_or_create(nome='Campo Toroidal Cardíaco', defaults={'descricao_tecnica': 'Campo magnético 5000x mais forte que o do cérebro.'})
        dna_celular = dna 

        conectar(coracao, campo_eletromagnetico, 'GERA', 'O coração gera um campo em forma de Toro (Donut) que se estende por 3 metros fora do corpo.')
        conectar(campo_eletromagnetico, dna_celular, 'ALTERA', 'Experimentos mostram que a coerência cardíaca (amor) pode alterar a conformação do DNA à distância (Efeito Fantasma do DNA).', 9)

        # === 4. A GLÂNDULA PINEAL PIEZOELÉTRICA ===
        pineal, _ = Orgao.objects.get_or_create(nome='Glândula Pineal', defaults={'funcao_biologica': 'Produção de Melatonina', 'representacao_emocional': 'Olho de Hórus / Visão Espiritual'})
        cristais, _ = Substancia.objects.get_or_create(nome='Cristais de Calcita', defaults={'tipo': 'MINERAL'})
        
        conectar(pineal, cristais, 'CONTEM', 'A Pineal é cheia de microcristais de calcita flutuantes.')
        conectar(cristais, consciencia, 'TRANSDUZ', 'Pelo efeito piezoelétrico, os cristais transformam vibração mecânica em sinal elétrico, agindo como uma antena wi-fi biológica.')

        # === 5. A ÁGUA ESTRUTURADA (Fase 4) ===
        agua_ez, _ = Substancia.objects.get_or_create(nome='Água EZ (Zona de Exclusão)', defaults={'tipo': 'NUTRIENTE', 'formula_quimica': 'H3O2'})
        mitocondria = Celula.objects.filter(nome__icontains='Mitocôndria').first()
        
        conectar(agua_ez, mitocondria, 'POTENCIALIZA', 'A água dentro das células não é H2O, mas H3O2 (cristal líquido). Ela age como uma bateria que carrega as mitocôndrias.', 9)

        self.stdout.write(self.style.SUCCESS('✨ Segredos Quânticos Revelados e Injetados.'))
