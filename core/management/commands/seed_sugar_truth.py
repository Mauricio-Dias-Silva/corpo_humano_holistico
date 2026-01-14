from django.core.management.base import BaseCommand
from anatomia.models import Orgao, SistemaCorporal
from metabolismo.models import Substancia, Alimento, Desequilibrio, ProcessoMetabolico
from psicologia.models import Emocao, EstadoMental
from core.models import RelacaoHolistica
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Injeta a Verdade sobre o Açúcar (A Melhor e Pior Droga).'

    def handle(self, *args, **kwargs):
        self.stdout.write("🍬 Revelando a Verdade sobre o Açúcar...")

        def conectar(origem, destino, tipo, desc, forca=10):
             if origem and destino:
                RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ContentType.objects.get_for_model(origem), origem_object_id=origem.id,
                    destino_content_type=ContentType.objects.get_for_model(destino), destino_object_id=destino.id,
                    tipo=tipo, defaults={'descricao': desc, 'forca': forca, 'fonte': 'Bioquímica Holística'}
                )
        
        # === A DROGA (Açúcar) ===
        acucar, _ = Alimento.objects.get_or_create(
            nome='Açúcar Refinado (Sacarose)',
            defaults={'grupo': 'TÓXICO', 'natureza_energetica': 'FRIO', 'dosha_predominante': 'Kapha'}
        )

        # === O CÉU (Dopamina & Prazer) ===
        dopamina = Substancia.objects.filter(nome__icontains='Dopamina').first()
        if not dopamina:
            dopamina, _ = Substancia.objects.get_or_create(nome='Dopamina', defaults={'tipo': 'NEUROTRANSMISSOR'})
            
        nervoso, _ = SistemaCorporal.objects.get_or_create(nome='Sistema Nervoso')
        accumbens, _ = Orgao.objects.get_or_create(nome='Núcleo Accumbens', defaults={'sistema': nervoso})
        prazer, _ = Emocao.objects.get_or_create(nome='Prazer Imediato', defaults={'polaridade': 'POSITIVA'})
        
        # Ciclo do Prazer
        conectar(acucar, accumbens, 'HIPER-ESTIMULA', 'O açúcar ilumina o Núcleo Accumbens 8x mais que a cocaína em ratos.', 10)
        conectar(acucar, dopamina, 'EXPLODE', 'Gera um pico massivo de dopamina, criando a sensação de "Melhor Droga".', 10)
        conectar(dopamina, prazer, 'GERA', 'Sensação fugaz de felicidade e recompensa.', 9)

        # === O INFERNO (Glicação & Inflamação) ===
        insulina, _ = Substancia.objects.get_or_create(nome='Insulina', defaults={'tipo': 'HORMONIO'})
        inflamacao, _ = ProcessoMetabolico.objects.get_or_create(nome='Inflamação Sistêmica Crônica')
        glicacao, _ = ProcessoMetabolico.objects.get_or_create(nome='Glicação (Envelhecimento)', defaults={'descricao_detalhada': 'Caramelização das proteínas (Colágeno).'})
        mitocondria = Orgao.objects.filter(nome__icontains='Mitocôndria').first()
        
        # Ciclo da Destruição
        conectar(acucar, insulina, 'DISPARA', 'Pico de insulina que leva à resistência (Diabetes Tipo 2).', 10)
        conectar(acucar, glicacao, 'CAUSA', 'O açúcar se une ao colágeno, tornando a pele e artérias rígidas ("Caramelização").', 9)
        conectar(acucar, inflamacao, 'ALIMENTA', 'O açúcar é o combustível principal da inflamação crônica.', 10)
        
        if mitocondria:
            conectar(acucar, mitocondria, 'DESTROI', 'O excesso de glicose gera EROs (Radicais Livres) que matam a mitocôndria.', 10)

        # Efeitos Mentais
        brain_fog, _ = EstadoMental.objects.get_or_create(nome='Névoa Mental (Brain Fog)')
        conectar(acucar, brain_fog, 'INDUZ', 'A queda abrupta de glicose (hipoglicemia reativa) causa confusão e lentidão.', 9)

        self.stdout.write(self.style.SUCCESS('🍬 A Doce e Amarga Verdade foi Injetada.'))
