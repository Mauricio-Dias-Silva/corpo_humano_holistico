from django.core.management.base import BaseCommand
from anatomia.models import Orgao, SistemaCorporal
from metabolismo.models import Substancia, Alimento, Desequilibrio, ProcessoMetabolico
from psicologia.models import Emocao, EstadoMental
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta Sabedoria Ancestral das Plantas (Fitoterapia Holística).'

    def handle(self, *args, **kwargs):
        self.stdout.write("🌿 Colhendo Ervas Sagradas...")

        def conectar(origem, destino, tipo, desc, forca=8):
             if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca, 'fonte': 'Fitoterapia Tradicional'}
                )
        
        # === ERVAS & PLANTAS ===
        ervas = [
            ('Camomila', 'BEBIDA', 'FRESCO', 'Calmante suave, digestiva'),
            ('Hortelã', 'BEBIDA', 'FRESCO', 'Abre vias respiratórias, refresca a mente'),
            ('Gengibre', 'VEGETAL', 'QUENTE', 'Aquece o corpo, anti-inflamatório potente'),
            ('Cúrcuma (Açafrão)', 'VEGETAL', 'MORNO', 'Antioxidante mestre, previne Alzheimer'),
            ('Valeriana', 'BEBIDA', 'MORNO', 'Sedativo natural profundo'),
            ('Alecrim', 'VEGETAL', 'QUENTE', 'Estimula a memória e o foco ("Erva da Alegria")'),
            ('Lavanda', 'BEBIDA', 'NEUTRO', 'Equilibra o sistema nervoso, antisséptico'),
            ('Dente-de-Leão', 'VEGETAL', 'FRIO', 'Desintoxica o Fígado profundamente'),
            ('Babosa (Aloe Vera)', 'VEGETAL', 'FRIO', 'Cicatrização, regeneração celular'),
            ('Ginseng', 'VEGETAL', 'QUENTE', 'Energia vital (Qi), adaptação ao estresse'),
            ('Ayahuasca (Cipó)', 'BEBIDA', 'QUENTE', 'Expansão da consciência, purga espiritual'),
        ]

        # Entidades-Alvo Existentes
        figado = Orgao.objects.filter(nome__icontains='Fígado').first()
        estomago = Orgao.objects.filter(nome__icontains='Estômago').first()
        cerebro = Orgao.objects.filter(nome__icontains='Cérebro').first()
        ansiedade = Emocao.objects.filter(nome__icontains='Ansiedade').first()
        memoria = Orgao.objects.filter(nome__icontains='Hipocampo').first() # Memória
        
        for nome, grupo, nat, desc_tec in ervas:
            planta, _ = Alimento.objects.get_or_create(
                nome=nome, 
                defaults={
                    'grupo': grupo, 
                    'natureza_energetica': nat, 
                    'dosha_predominante': 'Tridosha' # Simplificado
                }
            )
            
            # --- Conexões Específicas ---
            if 'Gengibre' in nome:
                inflamacao = ProcessoMetabolico.objects.filter(nome__icontains='Inflamação').first()
                conectar(planta, inflamacao, 'INIBE', 'O gingerol do gengibre bloqueia vias inflamatórias (COX-2).', 9)
            
            if 'Cúrcuma' in nome:
                curcumina, _ = Substancia.objects.get_or_create(nome='Curcumina', defaults={'tipo': 'FITOQUIMICO'})
                planta.compostos_ativos.add(curcumina)
                if cerebro: conectar(curcumina, cerebro, 'PROTEGE', 'A curcumina cruza a barreira hematoencefálica e limpa placas beta-amiloides.', 10)
                
            if 'Alecrim' in nome and memoria:
                conectar(planta, memoria, 'ESTIMULA', 'O cheiro do alecrim aumenta a retenção de memória em até 15%.', 8)
            
            if 'Dente-de-Leão' in nome and figado:
                conectar(planta, figado, 'CURA', 'Estimula o fluxo biliar e limpa toxinas hepáticas.', 9)

            if 'Valeriana' in nome or 'Camomila' in nome:
                gaba = Substancia.objects.filter(nome__icontains='GABA').first()
                if gaba: conectar(planta, gaba, 'ESTIMULA', 'Aumenta a disponibilidade de GABA no cérebro.', 8)

        self.stdout.write(self.style.SUCCESS('🌿 Sabedoria Herbal Injetada.'))
