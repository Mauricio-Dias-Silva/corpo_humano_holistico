from django.core.management.base import BaseCommand
from core.models import RelacaoHolistica
from anatomia.models import Orgao, SistemaCorporal
from psicologia.models import Emocao, Pensamento, EstadoMental
from metabolismo.models import ProcessoMetabolico
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta as leis Espirituais da Cura e Doenças Autoimunes.'

    def handle(self, *args, **kwargs):
        self.stdout.write("🙏 Injetando Conhecimento Espiritual & Autoimune...")
        
        def conectar(origem, destino, tipo, desc, forca=10):
            if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca}
                )

        # --- NOVAS ENTIDADES ---
        autoimune, _ = ProcessoMetabolico.objects.get_or_create(nome='Doença Autoimune', defaults={'descricao_tecnica': 'O corpo ataca a si mesmo.'})
        fibromialgia, _ = ProcessoMetabolico.objects.get_or_create(nome='Fibromialgia', defaults={'descricao_tecnica': 'Dor crônica generalizada.'})
        enxaqueca, _ = ProcessoMetabolico.objects.get_or_create(nome='Enxaqueca', defaults={'descricao_tecnica': 'Dor vascular cerebral intensa.'})
        
        culpa, _ = Emocao.objects.get_or_create(nome='Culpa', defaults={'polaridade': 'NEGATIVA', 'impacto_imediato': 'Peso nos ombros, auto-punição'})
        auto_rejeicao, _ = Pensamento.objects.get_or_create(padrao="Eu não sou bom o suficiente", defaults={'categoria': 'CRENCA_LIMITANTE'})
        perdao, _ = Emocao.objects.get_or_create(nome='Perdão', defaults={'polaridade': 'POSITIVA', 'impacto_imediato': 'Libertação, leveza'})
        fe, _ = EstadoMental.objects.get_or_create(nome='Fé Inabalável', defaults={'ondas_cerebrais': 'Gamma / Coerência'})

        # --- LÓGICA ESPIRITUAL DA DOENÇA ---
        
        # Autoimune (Lupus, Artrite, etc)
        conectar(auto_rejeicao, autoimune, 'CAUSA_EMOCIONAL', 'Se você se rejeita mentalmente, seu sistema imune aprende a rejeitar seu corpo biologicamente.')
        conectar(culpa, autoimune, 'ALIMENTA', 'A culpa busca punição. A doença autoimune é a forma física de auto-punição.')
        
        # Fibromialgia
        tencao_familiar = Pensamento.objects.create(padrao="Carrego o peso da família", categoria='CRENCA_LIMITANTE')
        conectar(tencao_familiar, fibromialgia, 'CAUSA_EMOCIONAL', 'Fibromialgia é frequentemente "o grito da dor emocional" não chorada. Fardos excessivos.')

        # Enxaqueca
        perfeccionismo = Pensamento.objects.create(padrao="Tem que ser perfeito", categoria='RUMINACAO')
        conectar(perfeccionismo, enxaqueca, 'CAUSA_EMOCIONAL', 'Raiva contida de não controlar tudo. Pressão excessiva sobre si mesmo.')
        
        # --- A CURA (Jesus & Buda) ---
        
        # O Milagre (Fé modifica Biologia)
        sistema_imune = SistemaCorporal.objects.filter(nome__icontains='Imune').first()
        conectar(fe, sistema_imune, 'POTENCIALIZA', 'A certeza absoluta (Fé) remove o estresse (Cortisol) instantaneamente, permitindo "milagres" imunológicos.')
        
        # O Desapego (Cura budista)
        apego = Emocao.objects.create(nome='Apego à Dor', polaridade='NEGATIVA', impacto_imediato='Contração')
        conectar(apego, ProcessoMetabolico.objects.get(nome__icontains='Inflamação'), 'ETERNIZA', 'Enquanto houver apego à história de vítima, a inflamação persiste.')
        
        conectar(perdao, autoimune, 'CURA', 'O auto-perdão cessa o ataque imune. Amar a si mesmo é o remédio para autoimunidade.')

        self.stdout.write(self.style.SUCCESS('✅ Leis Espirituais da Cura Injetadas.'))
