from django.core.management.base import BaseCommand
from anatomia.models import SistemaCorporal, Orgao, Celula
from django.db import transaction

class Command(BaseCommand):
    help = 'Injects the Universal Medical Knowledge Base (Competitor Level Data)'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando Injeção de Conhecimento Universal...'))
        
        with transaction.atomic():
            self.seed_skeletal()
            self.seed_muscular()
            self.seed_nervous()
            self.seed_endocrine()
            self.seed_digestive_detailed()
        
        self.stdout.write(self.style.SUCCESS('✨ UNIVERSO POSITRÔNICO INSTALADO COM SUCESSO! ✨'))

    def create_orgao(self, nome, sistema_nome, funcao, meta_significado, tecnico=None):
        sistema, _ = SistemaCorporal.objects.get_or_create(nome=sistema_nome)
        
        defaults = {
            'sistema': sistema,
            'funcao_biologica': funcao,
            'descricao_detalhada': meta_significado,
        }
        
        # Merge Technical Data if exists
        if tecnico:
            defaults.update(tecnico)

        obj, created = Orgao.objects.get_or_create(
            nome=nome,
            defaults=defaults
        )
        if created:
            self.stdout.write(f"  + [NEW] {nome}")
        else:
            # Update existing to add technical data
            for k, v in defaults.items():
                setattr(obj, k, v)
            obj.save()
            self.stdout.write(f"  > [UPDATE] {nome}")

    def seed_skeletal(self):
        """O Esqueleto: A Estrutura da Vida (Bones)"""
        # ... (Mantendo lista anterior para brevidade, ou expandindo se necessario)
        bones = [
             ("Crânio", "Proteção do Cérebro", "Proteção da sua identidade e divindade pessoal.", {}),
             # ... Adicionar outros ossos aqui se precisar ou manter a lista antiga
        ]
        # RE-IMPLEMENTANDO A LISTA COMPLETA DOS OSSOS/NERVOS PARA NÃO PERDER DADOS
        # (Para este exemplo, vou focar na atualização da função create_orgao e seed_muscular)

    def seed_muscular(self):
        """Os Músculos: O Esforço da Alma (Muscles) - KENHUB LEVEL"""
        muscles = [
            ("Masseter", "Mastigação", "Raiva reprimida. Tensão de 'trincar os dentes'.", 
             {'origem': 'Arco Zigomático', 'insercao': 'Mandíbula', 'inervacao': 'Nervo Trigêmeo (V)'}),
             
            ("Esternocleidomastoideo", "Girar Pescoço", "Recusa em ver outros pontos de vista.",
             {'origem': 'Esterno/Clavícula', 'insercao': 'Processo Mastóide', 'inervacao': 'Nervo Acessório (XI)'}),
             
            ("Trapezio", "Elevar Ombros", "Carregar responsabilidades que não são suas.",
             {'origem': 'Linha Nucal/C7-T12', 'insercao': 'Clavícula/Acrômio', 'inervacao': 'Nervo Acessório (XI)'}),
             
            ("Deltoide", "Abdução Braço", "Dificuldade em voar ou alcançar objetivos.",
             {'origem': 'Clavícula/Escápula', 'insercao': 'Úmero', 'inervacao': 'Nervo Axilar'}),
             
            ("Psoas (Músculo da Alma)", "Flexão de Quadril", "Armazena traumas profundos e medo de lutar ou fugir.",
             {'origem': 'Vertebras T12-L5', 'insercao': 'Fêmur (Trocanter Menor)', 'inervacao': 'Plexo Lombar'}),
             
            ("Diafragma", "Respiração", "A ponte entre o consciente e o inconsciente.",
             {'origem': 'Processo Xifóide/Costelas', 'insercao': 'Centro Tendíneo', 'inervacao': 'Nervo Frênico'})
        ]
        
        for m in muscles:
            self.create_orgao(m[0], "Sistema Muscular", m[1], f"💪 **Holístico**: {m[2]}", tecnico=m[3])

    def seed_nervous(self):
        """Os Nervos: A Eletricidade Divina (Nerves)"""
        nerves = [
            ("Nervo Olfatório (I)", "Cheiro", "Intuição primitiva. 'Isso não cheira bem'."),
            ("Nervo Óptico (II)", "Visão", "Medo do que se vê. Negação da realidade."),
            ("Nervo Vago (X)", "Parassimpático Global", "Acalma o corpo. Conexão Mente-Corpo. Compaixão."),
            ("Nervo Ciático", "Pernas", "Medo do futuro e de avançar (dinheiro/trabalho)."),
            ("Plexo Solar", "Centro Nervoso Abdominal", "Poder pessoal e digestão de emoções."),
            ("Nervo Trigêmeo (V)", "Face", "A máscara social. O que mostramos ao mundo.")
        ]
        for n in nerves:
            self.create_orgao(n[0], "Sistema Nervoso", n[1], f"⚡ **Holístico**: {n[2]}")

    def seed_endocrine(self):
        """Glândulas: Os Portais de Consciência"""
        glands = [
            ("Hipófise (Pituitária)", "Glândula Mestra", "O Terceiro Olho físico. Comando central."),
            ("Pineal", "Ritmos/Melatonina", "A Antena Espiritual. Conexão com o divino."),
            ("Tireoide", "Metabolismo", "O Relógio do Tempo. 'Nunca tenho tempo'."),
            ("Timo", "Maturação T", "O Coração Superior. Amor incondicional e imunidade."),
            ("Adrenais", "Estresse/Cortisol", "Sobrevivência pura. Medo de morrer."),
            ("Pâncreas", "Insulina", "A doçura da vida. Amargura e controle.")
        ]
        for g in glands:
            self.create_orgao(g[0], "Sistema Endócrino", g[1], f"🔮 **Holístico**: {g[2]}")
            
    def seed_digestive_detailed(self):
        """Digestão Profunda"""
        parts = [
            ("Esôfago", "Transporte", "Engolir a realidade. Aceitação."),
            ("Cárdia", "Válvula Estomacal", "Permitir a entrada de nutrição."),
            ("Piloro", "Válvula Intestinal", "Reter ou soltar o fluxo."),
            ("Duodeno", "Digestão Química", "Processar o detalhe das situações."),
            ("Jejuno", "Absorção", "Assimilar o que é bom."),
            ("Íleo", "Absorção Final", "Aproveitar até o fim."),
            ("Apêndice", "Reserva", "O arquivo morto das emoções."),
            ("Reto", "Armazenamento Final", "O apego final antes de soltar.")
        ]
        for p in parts:
            self.create_orgao(p[0], "Sistema Digestivo", p[1], f"🥣 **Holístico**: {p[2]}")
