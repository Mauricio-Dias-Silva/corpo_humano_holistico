from django.core.management.base import BaseCommand
from core.models import RelacaoHolistica
from anatomia.models import Orgao, Celula
from psicologia.models import Emocao, Pensamento
from metabolismo.models import ProcessoMetabolico, Substancia
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta conhecimento sobre Oncologia Holística.'

    def handle(self, *args, **kwargs):
        self.stdout.write("🦀 Mapeando a Oncologia Holística...")
        
        def conectar(origem, destino, tipo, desc, forca=10):
            if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca}
                )

        # Entidades
        cancer, _ = ProcessoMetabolico.objects.get_or_create(nome='Câncer (Neoplasia)', defaults={'descricao_tecnica': 'Crescimento celular desordenado e falha na apoptose.'})
        apoptose, _ = ProcessoMetabolico.objects.get_or_create(nome='Apoptose', defaults={'descricao_tecnica': 'Morte celular programada (suicídio celular benéfico).'})
        hipoxia, _ = ProcessoMetabolico.objects.get_or_create(nome='Hipóxia Celular', defaults={'descricao_tecnica': 'Baixo oxigênio no ambiente celular.'})
        
        magoa, _ = Emocao.objects.get_or_create(nome='Mágoa Profunda', defaults={'polaridade': 'NEGATIVA', 'impacto_imediato': 'Aperto no peito, nó na garganta'})
        ressentimento, _ = Emocao.objects.get_or_create(nome='Ressentimento', defaults={'polaridade': 'NEGATIVA', 'impacto_imediato': 'Acidez estomacal, tensão'})
        
        linfocito_t = Celula.objects.filter(nome__icontains='Linfócito T').first()
        acucar = Substancia.objects.filter(nome__icontains='Glicose').first()

        # Conexões
        # 1. Biológico
        conectar(hipoxia, cancer, 'CAUSA_FISICA', 'Células em ambiente sem oxigênio (ácido) mutam para sobreviver (Efeito Warburg).')
        conectar(apoptose, cancer, 'INIBE', 'O câncer acontece quando a Apoptose falha e a célula velha se recusa a morrer.')
        if acucar:
            conectar(acucar, cancer, 'ESTIMULA', 'Células cancerígenas consomem 15x mais glicose que células normais.')
        
        # 2. Imunológico
        if linfocito_t:
            conectar(linfocito_t, cancer, 'INIBE', 'As Células T Killer são responsáveis por identificar e destruir tumores.')
            
        # 3. Psicossomático
        conectar(magoa, cancer, 'CORRELACAO', 'Muitos autores holísticos associam tumores a mágoas antigas guardadas (cristalizadas).', 9)
        conectar(ressentimento, cancer, 'AGRAVA', 'O ressentimento ("sentir de novo") mantém o corpo em estado inflamatório crônico.', 9)

        self.stdout.write(self.style.SUCCESS('✅ Oncologia Holística Mapeada.'))
