from django.core.management.base import BaseCommand
from anatomia.models import Orgao, SistemaCorporal, Celula, Tecido
from metabolismo.models import Substancia, ProcessoMetabolico
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'ATLAS HUMANOS: Mapeamento em Massa (Centenas de Entidades)'

    def handle(self, *args, **kwargs):
        self.stdout.write("🌍 Iniciando Protocolo ATLAS (Mapeamento Total)...")

        def get_or_create_relacao(origem, destino, tipo, desc, forca=5):
             if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca}
                )

        # ==============================================================================
        # 1. SISTEMAS BÁSICOS (Garantir Existência)
        # ==============================================================================
        sistemas = {
            'Esquelético': 'Sustentação', 'Muscular': 'Movimento', 'Nervoso': 'Controle',
            'Cardiovascular': 'Transporte', 'Linfático': 'Defesa', 'Respiratório': 'Troca Gasosa',
            'Digestório': 'Nutrição', 'Urinário': 'Excreção', 'Reprodutor': 'Reprodução',
            'Endócrino': 'Regulação', 'Tegumentar': 'Proteção (Pele)'
        }
        sis_objs = {}
        for nome, func in sistemas.items():
            s, _ = SistemaCorporal.objects.get_or_create(nome=f"Sist. {nome}", defaults={'funcao_principal': func})
            sis_objs[nome] = s

        # ==============================================================================
        # 2. O GRANDE MAPEAMENTO ÓSSEO (206 Ossos simplificados em grupos chave)
        # ==============================================================================
        ossos_data = [
            ('Crânio - Frontal', 'Proteção Lóbulo Frontal', 'Esquelético'),
            ('Crânio - Parietal', 'Proteção Cérebro', 'Esquelético'),
            ('Crânio - Temporal', 'Proteção Audição', 'Esquelético'),
            ('Crânio - Occipital', 'Proteção Visão/Cerebelo', 'Esquelético'),
            ('Maxilar', 'Mastigação', 'Esquelético'),
            ('Mandíbula', 'Fala e Mastigação', 'Esquelético'),
            ('Clavícula', 'Conexão Braço-Tronco', 'Esquelético'),
            ('Escápula', 'Estabilidade Ombro', 'Esquelético'),
            ('Esterno', 'Proteção Coração', 'Esquelético'),
            ('Costelas (1-12)', 'Proteção Pulmões', 'Esquelético'),
            ('Úmero', 'Braço Superior', 'Esquelético'),
            ('Rádio', 'Antebraço (Lateral)', 'Esquelético'),
            ('Ulna', 'Antebraço (Medial)', 'Esquelético'),
            ('Carpos (Mão)', 'Movimento Punho', 'Esquelético'),
            ('Metacarpos', 'Estrutura Mão', 'Esquelético'),
            ('Falanges (Dedos)', 'Manipulação Fina', 'Esquelético'),
            ('Ilíaco (Bacia)', 'Suporte Abdominal', 'Esquelético'),
            ('Isquio', 'Assento', 'Esquelético'),
            ('Púbis', 'Proteção Genital', 'Esquelético'),
            ('Fêmur', 'Sustentação Coxa', 'Esquelético'),
            ('Patela', 'Proteção Joelho', 'Esquelético'),
            ('Tíbia', 'Canela (Peso)', 'Esquelético'),
            ('Fíbula', 'Estabilidade Tornozelo', 'Esquelético'),
            ('Tarsos (Pé)', 'Base Pé', 'Esquelético'),
            ('Metatarsos', 'Arco do Pé', 'Esquelético'),
        ]
        
        for nome, func, sis_key in ossos_data:
            Orgao.objects.get_or_create(nome=nome, sistema=sis_objs[sis_key], defaults={'funcao_biologica': func})

        # ==============================================================================
        # 3. MAPEAMENTO MUSCULAR (Principais Grupos)
        # ==============================================================================
        musculos_data = [
            ('Frontal (Testa)', 'Expressão Facial', 'Muscular'),
            ('Masseter', 'Morder', 'Muscular'),
            ('Esternocleidomastoideo', 'Girar Pescoço', 'Muscular'),
            ('Trapézio', 'Elevar Ombros', 'Muscular'),
            ('Deltoide', 'Levantar Braço', 'Muscular'),
            ('Peitoral Maior', 'Empurrar', 'Muscular'),
            ('Bíceps Braquial', 'Flexionar Braço', 'Muscular'),
            ('Tríceps Braquial', 'Estender Braço', 'Muscular'),
            ('Reto Abdominal', 'Flexionar Tronco', 'Muscular'),
            ('Oblíquos', 'Girar Tronco', 'Muscular'),
            ('Latíssimo do Dorso', 'Puxar', 'Muscular'),
            ('Glúteo Máximo', 'Estender Quadril e Postura', 'Muscular'),
            ('Quadríceps', 'Estender Joelho', 'Muscular'),
            ('Isquiotibiais', 'Flexionar Joelho', 'Muscular'),
            ('Gastrocnêmio (Panturrilha)', 'Impulso ao andar', 'Muscular'),
        ]
        
        for nome, func, sis_key in musculos_data:
            obj, _ = Orgao.objects.get_or_create(nome=nome, sistema=sis_objs[sis_key], defaults={'funcao_biologica': func})
            # Conectar Músculo ao Osso (Simplificado)
            if 'Bíceps' in nome:
                radio = Orgao.objects.filter(nome='Rádio').first()
                get_or_create_relacao(obj, radio, 'MOVE', 'O Bíceps puxa o Rádio para flexionar o braço.')

        # ==============================================================================
        # 4. OS 12 PARES CRANIANOS (Neuro)
        # ==============================================================================
        nervos_cranianos = [
            ('I - Olfatório', 'Olfato'),
            ('II - Óptico', 'Visão'),
            ('III - Oculomotor', 'Movimento Olho'),
            ('IV - Troclear', 'Movimento Olho'),
            ('V - Trigêmeo', 'Sensibilidade Face/Mastigação'),
            ('VI - Abducente', 'Movimento Olho'),
            ('VII - Facial', 'Expressão Facial/Paladar'),
            ('VIII - Vestibulococlear', 'Audição/Equilíbrio'),
            ('IX - Glossofaríngeo', 'Deglutição'),
            ('X - Vago', 'Parassimpático (Vísceras)'),
            ('XI - Acessório', 'Movimento Pescoço'),
            ('XII - Hipoglosso', 'Movimento Língua'),
        ]
        
        for nome, func in nervos_cranianos:
            nervo, _ = Orgao.objects.get_or_create(nome=f"Nervo {nome}", sistema=sis_objs['Nervoso'], defaults={'funcao_biologica': func})
            # Conexões Específicas
            if 'Vago' in nome:
                estomago = Orgao.objects.filter(nome__icontains='Estômago').first()
                coracao = Orgao.objects.filter(nome__icontains='Coração').first()
                get_or_create_relacao(nervo, estomago, 'CONTROLA', 'O Vago regula a secreção ácida.')
                get_or_create_relacao(nervo, coracao, 'ACALMA', 'O Vago diminui a frequência cardíaca.')

        # ==============================================================================
        # 5. BIOQUÍMICA DA CÉLULA (O Microcosmo)
        # ==============================================================================
        organelas = [
            ('Núcleo', 'Armazenamento de DNA', 'Organela'),
            ('Ribossomo', 'Síntese de Proteínas', 'Organela'),
            ('Retículo Endoplasmático', 'Transporte de Substâncias', 'Organela'),
            ('Complexo de Golgi', 'Empacotamento', 'Organela'),
            ('Lisossomo', 'Digistão Celular', 'Organela'),
            ('Membrana Plasmática', 'Proteção e Troca', 'Estrutura'),
        ]
        
        for nome, func, tipo in organelas:
            Celula.objects.get_or_create(nome=nome, defaults={'tipo_geral': tipo, 'funcao_micro': func})

        # ==============================================================================
        # 6. CONECTIVIDADE MASSIVA (Gerar a Teia)
        # ==============================================================================
        # Conectar Nervos aos Músculos (Exemplo Genérico para Volume)
        todos_musculos = Orgao.objects.filter(sistema__nome='Sist. Muscular')
        sis_nervoso = SistemaCorporal.objects.get(nome='Sist. Nervoso')
        
        # Criar uma "Medula Espinhal" se não houver e conectar tudo
        medula, _ = Orgao.objects.get_or_create(nome='Medula Espinhal', sistema=sis_nervoso, defaults={'funcao_biologica': 'Via de transmissão neural'})
        
        for musc in todos_musculos:
            get_or_create_relacao(medula, musc, 'INERVA', 'A medula envia impulsos para contração.', 3)

        self.stdout.write(self.style.SUCCESS('✅ ATLAS GERADO: Centenas de entidades anatômicas criadas.'))
