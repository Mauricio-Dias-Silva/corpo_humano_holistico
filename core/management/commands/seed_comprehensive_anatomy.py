from django.core.management.base import BaseCommand
from anatomia.models import Orgao, SistemaCorporal, Celula, Tecido
from metabolismo.models import Substancia, ProcessoMetabolico, Desequilibrio
from psicologia.models import Emocao, Pensamento
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Mapeamento Anatômico Total (Esqueleto, Cérebro Profundo, Coração, Células).'

    def handle(self, *args, **kwargs):
        self.stdout.write("💀 Iniciando Mapeamento Anatômico Total...")
        
        def conectar(origem, destino, tipo, desc, forca=8):
             if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca}
                )

        # === 1. SISTEMA ESQUELÉTICO (A Estrutura) ===
        sis_esqueletico, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Esquelético')
        
        # Células Ósseas
        osteoblasto, _ = Celula.objects.get_or_create(nome='Osteoblasto', defaults={'tipo_geral': 'Óssea', 'funcao_micro': 'Constrói osso novo (Deposição)'})
        osteoclasto, _ = Celula.objects.get_or_create(nome='Osteoclasto', defaults={'tipo_geral': 'Óssea', 'funcao_micro': 'Reabsorve osso velho (Degradação)'})
        
        # Ossos Principais
        femur, _ = Orgao.objects.get_or_create(nome='Fêmur', sistema=sis_esqueletico, defaults={'funcao_biologica': 'Sustentação da coxa, produção de sangue na medula', 'representacao_emocional': 'Capacidade de ir em frente, suportar o peso do futuro'})
        tibia, _ = Orgao.objects.get_or_create(nome='Tíbia', sistema=sis_esqueletico, defaults={'funcao_biologica': 'Sustentação da perna', 'representacao_emocional': 'Avançar com firmeza'})
        coluna_cervical, _ = Orgao.objects.get_or_create(nome='Coluna Cervical (C1-C7)', sistema=sis_esqueletico, defaults={'funcao_biologica': 'Suporte do crânio, flexibilidade do pescoço', 'representacao_emocional': 'Flexibilidade de pensamento, olhar para todos os lados'})
        coluna_lombar, _ = Orgao.objects.get_or_create(nome='Coluna Lombar (L1-L5)', sistema=sis_esqueletico, defaults={'funcao_biologica': 'Suporte de carga, movimento do tronco', 'representacao_emocional': 'Segurança financeira e suporte básico'})
        
        # Conexões
        medo = Emocao.objects.filter(nome__icontains='Medo').first()
        conectar(medo, coluna_lombar, 'ENFRAQUECE', 'O medo da escassez ataca a base da coluna (Lombar).', 10)
        
        # === 2. SISTEMA CARDIOVASCULAR (Detalhado) ===
        sis_cardio, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Cardiovascular')
        
        atrio_direito, _ = Orgao.objects.get_or_create(nome='Átrio Direito', sistema=sis_cardio, defaults={'funcao_biologica': 'Recebe sangue venoso do corpo'})
        ventriculo_esquerdo, _ = Orgao.objects.get_or_create(nome='Ventrículo Esquerdo', sistema=sis_cardio, defaults={'funcao_biologica': 'Bombeia sangue oxigenado para todo o corpo (Alta pressão)'})
        aorta, _ = Orgao.objects.get_or_create(nome='Aorta', sistema=sis_cardio, defaults={'funcao_biologica': 'Principal artéria do corpo'})
        
        cardiomiocito, _ = Celula.objects.get_or_create(nome='Cardiomiócito', defaults={'tipo_geral': 'Muscular Cardíaca', 'funcao_micro': 'Contração rítmica involuntária'})
        
        hipertensao = ProcessoMetabolico.objects.filter(nome__icontains='Hipertensão').first()
        conectar(hipertensao, ventriculo_esquerdo, 'SOBRECARREGA', 'A pressão alta força o ventrículo esquerdo a hipertrofiar até a falência.')

        # === 3. NEUROANATOMIA (O Cérebro em Partes) ===
        sis_nervoso = SistemaCorporal.objects.filter(nome__icontains='Nervoso').first()
        
        cortex_prefrontal, _ = Orgao.objects.get_or_create(nome='Córtex Pré-Frontal', sistema=sis_nervoso, defaults={'funcao_biologica': 'Tomada de decisão, controle de impulsos, personalidade', 'representacao_emocional': 'O "Adulto" da mente'})
        hipocampo, _ = Orgao.objects.get_or_create(nome='Hipocampo', sistema=sis_nervoso, defaults={'funcao_biologica': 'Memória de longo prazo e navegação espacial', 'representacao_emocional': 'Banco de dados da história pessoal'})
        cerebelo, _ = Orgao.objects.get_or_create(nome='Cerebelo', sistema=sis_nervoso, defaults={'funcao_biologica': 'Equilíbrio, coordenação motora fina'})
        
        cortisol = Substancia.objects.filter(nome__icontains='Cortisol').first()
        conectar(cortisol, hipocampo, 'ATROFIA', 'O estresse crônico (Cortisol) mata células do Hipocampo, causando perda de memória.', 10)

        # === 4. SISTEMA DIGESTIVO (Segmentos) ===
        sis_digestivo = SistemaCorporal.objects.filter(nome__icontains='Digestivo').first()
        
        esofago, _ = Orgao.objects.get_or_create(nome='Esôfago', sistema=sis_digestivo, defaults={'funcao_biologica': 'Transporte do bolo alimentar'})
        jejuno, _ = Orgao.objects.get_or_create(nome='Jejuno', sistema=sis_digestivo, defaults={'funcao_biologica': 'Principal local de absorção de nutrientes'})
        ileo, _ = Orgao.objects.get_or_create(nome='Íleo', sistema=sis_digestivo, defaults={'funcao_biologica': 'Absorção de B12 e sais biliares'})
        
        enterocito, _ = Celula.objects.get_or_create(nome='Enterócito', defaults={'tipo_geral': 'Intestinal', 'funcao_micro': 'Absorção de nutrientes (Microvilosidades)'})
        
        b12 = Substancia.objects.filter(nome__icontains='B12').first()
        conectar(ileo, b12, 'ABSORVE', 'O Íleo terminal é o único local capaz de absorver vitamina B12.')

        # === 5. BIOQUÍMICA AVANÇADA ===
        mitocondria, _ = Celula.objects.get_or_create(nome='Mitocôndria (Organela)', defaults={'tipo_geral': 'Organela', 'funcao_micro': 'Produção de ATP (Energia)'})
        atp, _ = Substancia.objects.get_or_create(nome='ATP (Adenosina Trifosfato)', defaults={'tipo': 'NUTRIENTE'})
        
        conectar(mitocondria, atp, 'PRODUZ', 'A Mitocôndria queima glicose/gordura para gerar ATP.')
        
        # Fadiga Crônica
        fadiga, _ = Desequilibrio.objects.get_or_create(substancia=atp, tipo='FALTA', defaults={'sintomas': 'Exaustão, neblina mental, fraqueza muscular', 'consequencias_holisticas': 'Falta de centelha vital.'})

        self.stdout.write(self.style.SUCCESS('✅ Mapeamento Anatômico Total Concluído!'))
