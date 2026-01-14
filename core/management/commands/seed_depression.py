from django.core.management.base import BaseCommand
from core.models import RelacaoHolistica
from anatomia.models import Orgao, SistemaCorporal
from psicologia.models import Emocao, EstadoMental
from metabolismo.models import Substancia, ProcessoMetabolico, Desequilibrio
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Adiciona a lógica específica da Depressão e Ansiedade.'

    def handle(self, *args, **kwargs):
        self.stdout.write("🌑 Mapeando a Melancolia e Depressão...")

        # Entidades
        depressao, _ = EstadoMental.objects.get_or_create(nome='Depressão', defaults={'ondas_cerebrais': 'Delta/Theta Excessivo'})
        serotonina = Substancia.objects.filter(nome__icontains='Serotonina').first()
        microbiota = Orgao.objects.filter(nome__icontains='Microbiota').first()
        intestino = Orgao.objects.filter(nome__icontains='Intestino Delgado').first()
        b12 = Substancia.objects.filter(nome__icontains='B12').first()
        
        # Helper Relação
        def lip(origem, destino, tipo, desc):
            if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': 9}
                )

        # Conexões da Depressão
        # 1. Falta de Serotonina -> Depressão
        deseq_s = Desequilibrio.objects.filter(substancia=serotonina, tipo='FALTA').first()
        if not deseq_s and serotonina:
            deseq_s = Desequilibrio.objects.create(substancia=serotonina, tipo='FALTA', nome_condicao='Depressão Serotoninérgica', sintomas='Tristeza, falta de vontade, sono ruim')
        
        # Serotonina -> Previne -> Depressão (Ou Falta -> Causa)
        # Vamos conectar a SUBSTANCIA diretamente para o Brain entender "Causas"
        # Mas o melhor é conectar o Desequilíbrio se fosse um objeto HolisticMixin, mas Desequilibrio não é Mixin no meu design atual (erro meu de design rápido, mas contornável).
        # Vamos conectar a SUBSTANCIA.
        
        lip(serotonina, depressao, 'INIBE', 'Níveis adequados de serotonina previnem o estado depressivo.')
        
        # 2. Intestino/Microbiota -> Serotonina -> Depressão
        lip(microbiota, serotonina, 'PRODUZ', 'Bactérias intestinais produzem 90% da serotonina.')
        lip(microbiota, depressao, 'CORRELACAO', 'Disbiose intestinal está fortemente ligada à depressão (Eixo Intestino-Cérebro).')
        
        # 3. Nutrientes
        lip(b12, depressao, 'INIBE', 'A falta de B12 causa danos neurológicos que simulam demência e depressão.')

        self.stdout.write(self.style.SUCCESS('✅ Lógica da Depressão Injetada!'))
