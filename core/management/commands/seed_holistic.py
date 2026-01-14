from django.core.management.base import BaseCommand
from core.models import RelacaoHolistica
from anatomia.models import Orgao, SistemaCorporal, Tecido
from psicologia.models import Emocao, Arquetipo, EstadoMental
from metabolismo.models import Substancia, ProcessoMetabolico
from simbologia.models import Chakra, Meridiano
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Popula o sistema com conhecimento Holístico, Médico e Esotérico.'

    def handle(self, *args, **kwargs):
        self.stdout.write("🧠 Iniciando a injeção de Conhecimento Holístico...")
        
        # === 1. SISTEMAS CORPORAIS ===
        self.stdout.write("Criando Sistemas Corporais...")
        sistemas = {
            'Nervoso': 'Controla e coordena as funções do corpo',
            'Cardiovascular': 'Transporta sangue, nutrientes e oxigênio',
            'Digestivo': 'Processa alimentos e absorve nutrientes',
            'Endócrino': 'Regula hormônios e metabolismo',
            'Respiratório': 'Troca gasosa e oxigenação',
            'Imunológico': 'Defesa contra patógenos',
            'Urinário': 'Filtragem e excreção',
            'Reprodutor': 'Reprodução e vitalidade',
            'Musculoesquelético': 'Estrutura e movimento',
            'Tegumentar': 'Proteção e sensibilidade (Pele)',
        }
        
        objs_sistema = {}
        for nome, func in sistemas.items():
            obj, _ = SistemaCorporal.objects.get_or_create(nome=nome, defaults={'funcao_principal': func})
            objs_sistema[nome] = obj

        # === 2. ORGÃOS & PECAS ===
        self.stdout.write("Criando Órgãos...")
        orgaos_data = [
            # Nervoso
            ('Cérebro', 'Nervoso', 'Processamento central', 'FOGO', 'Comando', 'Liderança'),
            ('Pineal', 'Nervoso', 'Produção de Melatonina', 'FOGO', 'Conexão Espiritual', 'Espiritualidade'),
            
            # Cardiovascular
            ('Coração', 'Cardiovascular', 'Bombeia sangue', 'FOGO', '11:00-13:00', 'Alegria, Amor Incondicional'),
            
            # Digestivo
            ('Estômago', 'Digestivo', 'Digestão ácida', 'TERRA', '07:00-09:00', 'Preocupação, Reflexão excessiva'),
            ('Fígado', 'Digestivo', 'Metabolismo e Desintoxicação', 'MADEIRA', '01:00-03:00', 'Raiva, Planejamento'),
            ('Intestino Grosso', 'Digestivo', 'Absorção de água e excreção', 'METAL', '05:00-07:00', 'Apego, Tristeza, Deixar ir'),
            ('Intestino Delgado', 'Digestivo', 'Absorção de nutrientes', 'FOGO', '13:00-15:00', 'Discernimento, Clareza'),
            
            # Endócrino
            ('Adrenais', 'Endócrino', 'Resposta ao estresse', 'AGUA', '', 'Medo, Sobrevivência'),
            ('Tireoide', 'Endócrino', 'Regulação metabólica', 'FOGO', '', 'Expressão, Comunicação'),
            
            # Respiratório
            ('Pulmão', 'Respiratório', 'Troca gasosa', 'METAL', '03:00-05:00', 'Tristeza, Melancolia'),
            
            # Urinário
            ('Rins', 'Urinário', 'Filtragem do sangue', 'AGUA', '17:00-19:00', 'Medo, Força de Vontade'),
        ]
        
        objs_orgao = {}
        for nome, sist_nome, func, elem, hora, emoc in orgaos_data:
            obj, _ = Orgao.objects.get_or_create(
                nome=nome, 
                defaults={
                    'sistema': objs_sistema.get(sist_nome),
                    'funcao_biologica': func,
                    'elemento_mtc': elem,
                    'horario_pico': hora,
                    'representacao_emocional': emoc
                }
            )
            objs_orgao[nome] = obj

        # === 3. EMOÇÕES ===
        self.stdout.write("Criando Emoções...")
        emocoes_data = [
            ('Raiva', 'NEGATIVA', 'Calor, tensão muscular, mandíbula travada'),
            ('Medo', 'NEGATIVA', 'Frio na barriga, tremedeira, paralisia'),
            ('Alegria', 'POSITIVA', 'Expansão no peito, leveza'),
            ('Tristeza', 'NEGATIVA', 'Peso no peito, falta de ar, cansaço'),
            ('Preocupação', 'NEGATIVA', 'Nó no estômago, mente agitada'),
            ('Amor', 'POSITIVA', 'Calor suave, coerência cardíaca'),
            ('Ansiedade', 'NEGATIVA', 'Taquicardia, respiração curta'),
            ('Gratidão', 'POSITIVA', 'Paz profunda, relaxamento'),
        ]
        
        objs_emocao = {}
        for nome, pol, imp in emocoes_data:
            obj, _ = Emocao.objects.get_or_create(nome=nome, defaults={'polaridade': pol, 'impacto_imediato': imp})
            objs_emocao[nome] = obj
            
        # === 4. CHAKRAS ===
        self.stdout.write("Criando Chakras...")
        chakras_data = [
            ('Básico (Muladhara)', 'Vermelho', 'Base da coluna'),
            ('Sacral (Swadhisthana)', 'Laranja', 'Abaixo do umbigo'),
            ('Plexo Solar (Manipura)', 'Amarelo', 'Boca do estômago'),
            ('Cardíaco (Anahata)', 'Verde', 'Centro do peito'),
            ('Laríngeo (Vishuddha)', 'Azul Claro', 'Garganta'),
            ('Frontal (Ajna)', 'Índigo', 'Entre as sobrancelhas'),
            ('Coronário (Sahasrara)', 'Violeta/Branco', 'Topo da cabeça'),
        ]
        
        objs_chakra = {}
        for nome, cor, loc in chakras_data:
            obj, _ = Chakra.objects.get_or_create(nome=nome, defaults={'cor': cor, 'localizacao': loc})
            objs_chakra[nome] = obj

        # === 5. BIOQUÍMICA ===
        self.stdout.write("Criando Substâncias...")
        subs_data = [
            ('Cortisol', 'HORMONIO'),
            ('Adrenalina', 'HORMONIO'),
            ('Serotonina', 'NEUROTRANSMISSOR'),
            ('Dopamina', 'NEUROTRANSMISSOR'),
            ('Melatonina', 'HORMONIO'),
            ('Ocitocina', 'HORMONIO'),
        ]
        objs_substancia = {}
        for nome, tipo in subs_data:
            obj, _ = Substancia.objects.get_or_create(nome=nome, defaults={'tipo': tipo})
            objs_substancia[nome] = obj

        # === 6. CONECTANDO TUDO (A MÁGICA) ===
        self.stdout.write("🔗 Criando Conexões Holísticas (Sinapses do Sistema)...")
        
        def conectar(origem, destino, tipo, desc, forca=5):
            if not origem or not destino:
                return
            
            ct_origem = ContentType.objects.get_for_model(origem)
            ct_destino = ContentType.objects.get_for_model(destino)
            
            RelacaoHolistica.objects.get_or_create(
                origem_content_type=ct_origem,
                origem_object_id=origem.id,
                destino_content_type=ct_destino,
                destino_object_id=destino.id,
                tipo=tipo,
                defaults={
                    'descricao': desc,
                    'forca': forca
                }
            )

        # -- Conexões Psicossomáticas --
        conectar(objs_emocao['Raiva'], objs_orgao['Fígado'], 'CAUSA_FISICA', 'A raiva reprimida estagna o Qi do Fígado, causando tensão e problemas digestivos.', 9)
        conectar(objs_emocao['Medo'], objs_orgao['Rins'], 'CAUSA_FISICA', 'O medo excessivo esgota a energia vital (Jing) armazenada nos Rins.', 9)
        conectar(objs_emocao['Preocupação'], objs_orgao['Estômago'], 'CAUSA_FISICA', 'O excesso de pensamento prejudica a função de transporte e transformação do Baço/Estômago.', 8)
        conectar(objs_emocao['Tristeza'], objs_orgao['Pulmão'], 'CAUSA_FISICA', 'A tristeza consome o Qi do Pulmão, enfraquecendo a respiração e a imunidade.', 8)
        conectar(objs_emocao['Alegria'], objs_orgao['Coração'], 'ESTIMULA', 'A alegria moderada nutre o Coração, mas a euforia excessiva pode dispersar o Qi.', 10)
        
        # -- Conexões Bioquímicas x Emoções --
        conectar(objs_substancia['Cortisol'], objs_emocao['Ansiedade'], 'CORRELACAO', 'Níveis altos de cortisol estão diretamente ligados a estados de ansiedade.', 9)
        conectar(objs_substancia['Serotonina'], objs_emocao['Alegria'], 'ESTIMULA', 'Neurotransmissor chave para regulação do humor e felicidade.', 10)
        conectar(objs_substancia['Adrenalina'], objs_emocao['Medo'], 'CORRELACAO', 'Liberada na resposta de luta ou fuga.', 10)
        conectar(objs_substancia['Ocitocina'], objs_emocao['Amor'], 'CORRELACAO', 'Hormônio do vínculo e do afeto.', 10)

        # -- Conexões Chakras x Órgãos --
        conectar(objs_chakra['Básico (Muladhara)'], objs_orgao['Adrenais'], 'ESTIMULA', 'O chakra básico rege a sobrevivência e as supra-renais.', 9)
        conectar(objs_chakra['Plexo Solar (Manipura)'], objs_orgao['Estômago'], 'ESTIMULA', 'Centro do poder pessoal, digestão física e emocional.', 9)
        conectar(objs_chakra['Cardíaco (Anahata)'], objs_orgao['Coração'], 'ESTIMULA', 'Centro do amor e conexão.', 10)
        conectar(objs_chakra['Frontal (Ajna)'], objs_orgao['Pineal'], 'ESTIMULA', 'A glândula pineal é fisicamente associada ao terceiro olho.', 10)
        
        self.stdout.write(self.style.SUCCESS('✅ Injeção de Conhecimento Concluída com Sucesso! O corpo está vivo.'))
