from django.core.management.base import BaseCommand
from anatomia.models import Orgao, SistemaCorporal, Celula
from metabolismo.models import Substancia, ProcessoMetabolico, Desequilibrio
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta dados profundos baseados em bibliografia médica (Guyton, Gray, Harrison).'

    def handle(self, *args, **kwargs):
        self.stdout.write("📚 Abrindo a Enciclopédia Médica...")

        # --- HELPERS ---
        def get_mod(model, nome): return model.objects.filter(nome__icontains=nome).first()
        
        def criar_relacao(origem, destino, tipo, desc, forca=8):
            if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca}
                )

        # === 1. SISTEMA NERVOSO (Detalhado) ===
        sis_nervoso, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Nervoso', defaults={'funcao_principal': 'Controle e Comunicação Rápida'})
        
        # Estruturas do Tronco Encefálico & Cérebro
        hipotalamo, _ = Orgao.objects.get_or_create(nome='Hipotálamo', sistema=sis_nervoso, defaults={'funcao_biologica': 'Homeostase, Controle Endócrino, Temperatura', 'representacao_emocional': 'Centro dos Instintos Básicos'})
        amigdala, _ = Orgao.objects.get_or_create(nome='Amígdala Cerebral', sistema=sis_nervoso, defaults={'funcao_biologica': 'Processamento do Medo e Memória Emocional', 'representacao_emocional': 'Alerta de Perigo'})
        nervo_vago, _ = Orgao.objects.get_or_create(nome='Nervo Vago', sistema=sis_nervoso, defaults={'funcao_biologica': 'Controle Parassimpático (Digestão, Frequência Cardíaca)', 'representacao_emocional': 'Conexão Mente-Corpo, Calma'})

        # === 2. SISTEMA ENDÓCRINO (Eixo HPA e HPT) ===
        sis_endocrino, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Endócrino', defaults={'funcao_principal': 'Regulação Hormonal de Longo Prazo'})
        
        hipofise, _ = Orgao.objects.get_or_create(nome='Hipófise (Pituitária)', sistema=sis_endocrino, defaults={'funcao_biologica': 'Glândula Mestra, Secreção de TSH, ACTH, GH', 'representacao_emocional': 'Comando Superior'})
        
        # Hormônios Específicos
        tsh, _ = Substancia.objects.get_or_create(nome='TSH (Tireotrofina)', defaults={'tipo': 'HORMONIO'})
        t3, _ = Substancia.objects.get_or_create(nome='T3 (Triiodotironina)', defaults={'tipo': 'HORMONIO'})
        gh, _ = Substancia.objects.get_or_create(nome='GH (Hormônio do Crescimento)', defaults={'tipo': 'HORMONIO'})

        # Relações do Eixo
        criar_relacao(hipotalamo, hipofise, 'ESTIMULA', 'O Hipotálamo envia sinais para a Hipófise comandar o corpo (Eixo Hipotálamo-Hipófise).', 10)
        criar_relacao(hipofise, tsh, 'PRODUZ', 'A Hipófise secreta TSH para ativar a Tireoide.')
        tireoide = get_mod(Orgao, 'Tireoide')
        if tireoide:
            criar_relacao(tsh, tireoide, 'ESTIMULA', 'O TSH sinaliza a Tireoide para produzir T3 e T4.')
            criar_relacao(tireoide, t3, 'PRODUZ', 'A Tireoide converte T4 em T3, a forma ativa que acelera o metabolismo.')

        # === 3. SISTEMA DIGESTIVO (Fisiologia Fina) ===
        sis_digestivo, _ = SistemaCorporal.objects.get_or_create(nome='Sist. Digestivo')
        
        duodeno, _ = Orgao.objects.get_or_create(nome='Duodeno', sistema=sis_digestivo, defaults={'funcao_biologica': 'Recebe quimo, bile e suco pancreático. Início da absorção.', 'representacao_emocional': 'Capacidade de aceitar o novo'})
        microbiota, _ = Orgao.objects.get_or_create(nome='Microbiota Intestinal', sistema=sis_digestivo, defaults={'funcao_biologica': 'Simbiose bacteriana, imunidade, produção de serotonina', 'representacao_emocional': 'Intuição visceral'})
        
        # O Intestino produz Serotonina!
        serotonina = get_mod(Substancia, 'Serotonina')
        if serotonina:
            criar_relacao(microbiota, serotonina, 'PRODUZ', 'Cerca de 90% da serotonina do corpo é produzida pelas células enterocromafins e microbiota.', 9)

        # === 4. PATOLOGIA (Doenças comuns) ===
        # Diabetes Tipo 2
        insulina = get_mod(Substancia, 'Insulina')
        res_insulinica, _ = ProcessoMetabolico.objects.get_or_create(nome="Resistência Insulínica", defaults={'descricao_tecnica': 'Células param de responder à insulina, elevando glicemia.'})
        diabetes, _ = ProcessoMetabolico.objects.get_or_create(nome="Diabetes Tipo 2")
        
        criar_relacao(insulina, res_insulinica, 'CAUSA_FISICA', 'Níveis crônicos altos de insulina levam à desensibilização dos receptores (Downregulation).')
        criar_relacao(res_insulinica, diabetes, 'EVOLUI_PARA', 'Se não tratada, a resistência evolui para falência pancreática e Diabetes.')
        
        # Hipertensão
        adrenalina = get_mod(Substancia, 'Adrenalina')
        vasoconstricao, _ = ProcessoMetabolico.objects.get_or_create(nome="Vasoconstrição Periférica")
        hipertensao, _ = ProcessoMetabolico.objects.get_or_create(nome="Hipertensão Arterial")
        
        criar_relacao(adrenalina, vasoconstricao, 'CAUSA_FISICA', 'Adrenalina contrai os vasos sanguíneos para aumentar pressão na luta/fuga.')
        criar_relacao(vasoconstricao, hipertensao, 'AGRAVA', 'Vasos contraídos aumentam a resistência vascular periférica.')

        self.stdout.write(self.style.SUCCESS('✅ Dados de Enciclopédia Médica Injetados com Sucesso!'))
