from django.core.management.base import BaseCommand
from anatomia.models import Orgao, SistemaCorporal, Celula, Tecido
from metabolismo.models import Substancia, ProcessoMetabolico, Desequilibrio, Alimento
from psicologia.models import Emocao, Pensamento, Arquetipo, EstadoMental
from simbologia.models import Chakra
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeção de Conhecimento Onisciente (Medicina, Psicossomática, MTC, Nutrição Avançada).'

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Iniciando Protocolo OMNISCIÊNCIA...")
        
        def conectar(origem, destino, tipo, desc, forca=8):
             if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca}
                )

        # ==============================================================================
        # 1. SISTEMA IMUNE & LINFÁTICO (A Defesa)
        # ==============================================================================
        self.stdout.write("🛡️ Mapeando Imunidade...")
        sis_imune, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Imunológico', defaults={'funcao_principal': 'Defesa e Limpeza', 'cor_associada': 'Branco'})
        
        # Células
        leucocito, _ = Celula.objects.get_or_create(nome='Leucócito (Geral)', defaults={'tipo_geral': 'Imune', 'funcao_micro': 'Defesa geral'})
        linfocito_t, _ = Celula.objects.get_or_create(nome='Linfócito T', defaults={'tipo_geral': 'Imune', 'funcao_micro': 'Combate vírus e câncer. O "General" da defesa.'})
        macrofago, _ = Celula.objects.get_or_create(nome='Macrófago', defaults={'tipo_geral': 'Imune', 'funcao_micro': 'Engole bactérias e restos celulares (Fagocitose).'})
        
        # Órgãos
        timo, _ = Orgao.objects.get_or_create(nome='Timo', sistema=sis_imune, defaults={'funcao_biologica': 'Maturação de Linfócitos T', 'representacao_emocional': 'Vontade de viver, identidade imunológica', 'elemento_mtc': 'FOGO'})
        baco, _ = Orgao.objects.get_or_create(nome='Baço', sistema=sis_imune, defaults={'funcao_biologica': 'Filtragem do sangue e reserva imune', 'representacao_emocional': 'Obsessão, Preocupação (MTC)', 'elemento_mtc': 'TERRA'})

        # Substâncias (Citocinas)
        cortisol = Substancia.objects.filter(nome__icontains='Cortisol').first()
        interleucina, _ = Substancia.objects.get_or_create(nome='Interleucina-6 (Inflamação)', defaults={'tipo': 'TOXINA'}) # Simplificado como toxina no excesso

        # Lógica Imune
        conectar(timo, linfocito_t, 'PRODUZ', 'O Timo treina os Linfócitos T para distinguir o "Eu" do "Invasor".')
        conectar(cortisol, timo, 'INIBE', 'O estresse crônico (Cortisol) encolhe o Timo e mata Linfócitos T.', 10)
        conectar(baco, macrofago, 'ARMAZENA', 'O Baço é o quartel-general dos macrófagos.')

        # ==============================================================================
        # 2. NEUROCIÊNCIA AVANÇADA (A Química da Mente)
        # ==============================================================================
        self.stdout.write("🧠 Mapeando Neurotransmissores...")
        
        gaba, _ = Substancia.objects.get_or_create(nome='GABA', defaults={'tipo': 'NEUROTRANSMISSOR'})
        glutamato, _ = Substancia.objects.get_or_create(nome='Glutamato', defaults={'tipo': 'NEUROTRANSMISSOR'})
        aceticolina, _ = Substancia.objects.get_or_create(nome='Acetilcolina', defaults={'tipo': 'NEUROTRANSMISSOR'})
        
        # Desequilíbrios
        Desequilibrio.objects.get_or_create(substancia=gaba, tipo='FALTA', defaults={'sintomas': 'Ansiedade incontrolável, tremores, insônia', 'consequencias_holisticas': 'Mente que não desliga.'})
        Desequilibrio.objects.get_or_create(substancia=aceticolina, tipo='FALTA', defaults={'sintomas': 'Perda de memória, Alzheimer, falta de foco', 'consequencias_holisticas': 'Desconexão com o presente.'})
        
        # Alimentos & Neuro
        cha_verde, _ = Alimento.objects.get_or_create(nome='Chá Verde', defaults={'grupo': 'BEBIDA', 'natureza_energetica': 'FRESCO'})
        l_teanina, _ = Substancia.objects.get_or_create(nome='L-Teanina', defaults={'tipo': 'NUTRIENTE'})
        cha_verde.compostos_ativos.add(l_teanina)
        
        conectar(l_teanina, gaba, 'ESTIMULA', 'A L-Teanina aumenta a produção de GABA, gerando relaxamento alerta.', 9)

        # ==============================================================================
        # 3. PSICOSSOMÁTICA (Louise Hay / Linguagem do Corpo)
        # ==============================================================================
        self.stdout.write("🔮 Mapeando Psicossomática...")
        
        sis_ossea, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Esquelético')
        coluna, _ = Orgao.objects.get_or_create(nome='Coluna Vertebral', sistema=sis_ossea, defaults={'funcao_biologica': 'Sustentação', 'representacao_emocional': 'O suporte da vida'})
        joelhos, _ = Orgao.objects.get_or_create(nome='Joelhos', sistema=sis_ossea, defaults={'funcao_biologica': 'Articulação de movimento', 'representacao_emocional': 'Ego e Orgulho. Capacidade de se curvar/adaptar.'})
        
        medo = Emocao.objects.filter(nome__icontains='Medo').first()
        orgulho, _ = Emocao.objects.get_or_create(nome='Orgulho Rígido', defaults={'polaridade': 'NEGATIVA', 'impacto_imediato': 'Rigidez muscular'})
        
        conectar(medo, coluna, 'ENFRAQUECE', 'Falta de apoio financeiro/emocional reflete em dores na lombar (Medo da falta).', 9)
        conectar(orgulho, joelhos, 'BLOQUEIA', 'Inflexibilidade e ego rígido causam problemas nos joelhos.', 9)

        # ==============================================================================
        # 4. MTC - O CICLO DOS 5 ELEMENTOS
        # ==============================================================================
        self.stdout.write("☯️ Mapeando 5 Elementos...")
        
        rim = Orgao.objects.filter(nome__icontains='Rins').first()      # Água
        figado = Orgao.objects.filter(nome__icontains='Fígado').first() # Madeira
        coracao = Orgao.objects.filter(nome__icontains='Coração').first() # Fogo
        estomago = Orgao.objects.filter(nome__icontains='Estômago').first() # Terra
        pulmao = Orgao.objects.filter(nome__icontains='Pulmão').first() # Metal
        
        # Ciclo de Geração (Mãe nutre Filho)
        conectar(rim, figado, 'ESTIMULA', 'Ciclo MTC: Água nutre Madeira. Rins fortes nutrem o Fígado.', 8)
        conectar(figado, coracao, 'ESTIMULA', 'Ciclo MTC: Madeira nutre Fogo. O Fígado fornece sangue ao Coração.', 8)
        
        # Ciclo de Controle (Avó controla Neto)
        conectar(figado, estomago, 'INIBE', 'Ciclo MTC: Madeira controla Terra. Raiva (Fígado) ataca o Estômago (Gastrite).', 10)
        conectar(rim, coracao, 'INIBE', 'Ciclo MTC: Água controla Fogo. O medo apaga a alegria.', 8)

        # ==============================================================================
        # 5. NUTRIÇÃO AVANÇADA (Vitaminas e Minerais)
        # ==============================================================================
        vit_d, _ = Substancia.objects.get_or_create(nome='Vitamina D (Sol)', defaults={'tipo': 'HORMONIO'}) # Tecnicamente hormônio
        zinco, _ = Substancia.objects.get_or_create(nome='Zinco', defaults={'tipo': 'MINERAL'})
        omega3, _ = Substancia.objects.get_or_create(nome='Omega-3', defaults={'tipo': 'NUTRIENTE'})
        
        Desequilibrio.objects.get_or_create(substancia=vit_d, tipo='FALTA', defaults={'sintomas': 'Imunidade baixa, depressão, ossos fracos', 'consequencias_holisticas': 'Perda da luz interior.'})
        Desequilibrio.objects.get_or_create(substancia=zinco, tipo='FALTA', defaults={'sintomas': 'Queda de cabelo, baixa testosterona, unhas fracas', 'consequencias_holisticas': 'Perda do olfato/paladar pela vida.'})
        
        peixe, _ = Alimento.objects.get_or_create(nome='Peixe Gordo (Salmão)', defaults={'grupo': 'PROTEINA_ANIMAL', 'natureza_energetica': 'MORNO'})
        peixe.compostos_ativos.add(omega3)
        peixe.compostos_ativos.add(vit_d)
        
        cerebro = Orgao.objects.filter(nome__icontains='Cérebro').first()
        conectar(omega3, cerebro, 'CURA', 'O cérebro é 60% gordura. Omega-3 restaura a fluidez da membrana neuronal.', 9)
        conectar(omega3, ProcessoMetabolico.objects.get(nome__icontains='Inflamação'), 'INIBE', 'Omega-3 é um potente anti-inflamatório natural.', 10)

        self.stdout.write(self.style.SUCCESS('✅ PROTOCOLO OMNISCIÊNCIA CONCLUÍDO.'))
