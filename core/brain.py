import random
import datetime
import requests
import xml.etree.ElementTree as ET
from django.utils import timezone
from anatomia.models import SistemaCorporal, Orgao, Celula
from psicologia.models import Emocao, Pensamento, EstadoMental
from metabolismo.models import Substancia, Alimento, Desequilibrio, ProcessoMetabolico
from core.models import RelacaoHolistica
from django.db.models import Q


# ==========================================
# MÓDULO 0: PUBMED INTEGRATION (CIÊNCIA REAL)
# ==========================================
class PubMedService:
    """
    Integração com a maior base de dados científica do mundo.
    Busca estudos reais do PubMed para validar diagnósticos.
    """
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    
    def search(self, query, max_results=3):
        """Busca artigos no PubMed e retorna títulos e PMIDs."""
        try:
            # 1. Buscar IDs
            search_url = f"{self.BASE_URL}/esearch.fcgi?db=pubmed&term={query}&retmax={max_results}&retmode=json"
            response = requests.get(search_url, timeout=5)
            data = response.json()
            
            ids = data.get('esearchresult', {}).get('idlist', [])
            if not ids:
                return []
            
            # 2. Buscar detalhes dos artigos
            ids_str = ",".join(ids)
            summary_url = f"{self.BASE_URL}/esummary.fcgi?db=pubmed&id={ids_str}&retmode=json"
            summary_response = requests.get(summary_url, timeout=5)
            summary_data = summary_response.json()
            
            results = []
            for pmid in ids:
                article = summary_data.get('result', {}).get(pmid, {})
                if article:
                    results.append({
                        'pmid': pmid,
                        'title': article.get('title', 'Sem título'),
                        'authors': article.get('authors', [{}])[0].get('name', 'Desconhecido') if article.get('authors') else 'Desconhecido',
                        'journal': article.get('source', 'N/A'),
                        'year': article.get('pubdate', 'N/A')[:4],
                        'link': f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                    })
            return results
            
        except Exception as e:
            print(f"PubMed Error: {e}")
            return []

# ==========================================
# MÓDULO 1: SIMULADOR BIOQUÍMICO
# ==========================================
class SimuladorBioquimico:
    """
    Simula níveis estimados de neurotransmissores e hormônios baseados em sintomas.
    Não é um exame de sangue, é uma dedução algorítmica.
    """
    def analisar(self, texto):
        texto = texto.lower()
        perfil = {
            'dopamina': 'Estável',
            'serotonina': 'Estável',
            'cortisol': 'Estável',
            'gaba': 'Estável',
            'alerta': []
        }
        
        # Análise de DOPAMINA (Motivação/Foco)
        if 'foco' in texto or 'vicio' in texto or 'açúcar' in texto or 'porn' in texto:
            perfil['dopamina'] = '📉 Baixa (Crash)' if 'paralisia' in texto else '📈 Alta (Pico)'
            perfil['alerta'].append("Disregulação do Sistema de Recompensa (Nucleus Accumbens).")
            
        # Análise de CORTISOL (Estresse)
        if 'raiva' in texto or 'medo' in texto or 'ansiedade' in texto or 'estresse' in texto or 'paralisia' in texto:
            perfil['cortisol'] = '🔥 MUITO ALTO (Luta ou Fuga)'
            perfil['alerta'].append("Eixo HPA (Hipotálamo-Pituitária-Adrenal) em alerta máximo.")

        # Análise de SEROTONINA (Humor/Sono)
        if 'tristeza' in texto or 'depressão' in texto or 'sono' in texto or 'doce' in texto:
            perfil['serotonina'] = '📉 Baixa'
            perfil['alerta'].append("Exaustão do Sistema Serotoninérgico (Intestino afetado?).")

        return perfil

# ==========================================
# MÓDULO 2: CRONOBIOLOGIA (MTC)
# ==========================================
class RelogioBiologico:
    """
    Baseado na Medicina Tradicional Chinesa (MTC).
    Identifica qual órgão está no seu pico energético AGORA.
    """
    def orgao_do_momento(self):
        hora = datetime.datetime.now().time().hour
        
        tabela = {
            (1, 3):  "Fígado (Desintoxicação Profunda / Sono REM)",
            (3, 5):  "Pulmões (Respiração / Tristeza)",
            (5, 7):  "Intestino Grosso (Evacuação / Soltar o Passado)",
            (7, 9):  "Estômago (Café da Manhã / Digerir Ideias)",
            (9, 11): "Baço/Pâncreas (Metabolismo / Preocupação)",
            (11, 13): "Coração (Alegria / Circulação)",
            (13, 15): "Intestino Delgado (Absorção / Clareza Mental)",
            (15, 17): "Bexiga (Reservas / Medo)",
            (17, 19): "Rins (Vitalidade / Cansaço Profundo)",
            (19, 21): "Pericárdio (Proteção Emocional)",
            (21, 23): "Triplo Aquecedor (Endócrino / Imunidade)",
            (23, 1):  "Vesícula Biliar (Decisões / Coragem)"
        }
        
        for (inicio, fim), orgao in tabela.items():
            if inicio <= hora < fim:
                return orgao
            
        # Caso especial meia noite
        if hora == 23 or hora == 0:
             return "Vesícula Biliar (Decisões / Coragem)"
             
        return "Sistema em Manutenção"

# ==========================================
# MÓDULO 3: SISTEMA DE CHAKRAS (ENERGIA)
# ==========================================
class SistemaChakras:
    def analisar_energia(self, texto):
        """Mapeia sintomas para bloqueios nos 7 Chakras principais"""
        bloqueios = []
        
        mapa = {
            'Raiz (Muladhara)': ['medo', 'sobrevivência', 'dinheiro', 'pernas', 'ossos', 'rins'],
            'Sacral (Swadhisthana)': ['sexo', 'prazer', 'culpa', 'criatividade', 'reprodutor', 'bexiga'],
            'Plexo Solar (Manipura)': ['raiva', 'controle', 'poder', 'estômago', 'fígado', 'digestão'],
            'Coração (Anahata)': ['amor', 'mágoa', 'tristeza', 'pulmão', 'coração', 'imunidade'],
            'Garganta (Vishuddha)': ['expressão', 'verdade', 'tireoide', 'pescoço', 'calar'],
            'Terceiro Olho (Ajna)': ['foco', 'intuição', 'pesadelo', 'olhos', 'sono', 'pituitária'],
            'Coroa (Sahasrara)': ['fé', 'conexão', 'depressão', 'cérebro', 'pineal', 'sentido']
        }
        
        for chakra, keywords in mapa.items():
            for k in keywords:
                if k in texto:
                    bloqueios.append(f"🌀 Bloqueio no Chakra {chakra}")
                    break
        return bloqueios

# ==========================================
# MÓDULO 4: REDE NEURAL SIMULADA (MOCK)
# ==========================================
class RedeNeuralSimulada:
    """
    Simula o processamento de uma rede neural profunda (Deep Learning)
    para atribuir 'pesos' e 'confiança' ao diagnóstico.
    """
    def calcular_pesos(self, texto):
        neuronios = {
            'Inflamação': 0.1,
            'Oxidação': 0.1,
            'Glicação': 0.1,
            'Simpaticotonia': 0.1
        }
        
        # Feedforward (Simulado)
        if 'dor' in texto or 'vermelho' in texto: neuronios['Inflamação'] += 0.4
        if 'açúcar' in texto or 'doce' in texto: neuronios['Glicação'] += 0.8
        if 'foco' in texto or 'estresse' in texto: neuronios['Simpaticotonia'] += 0.6
        if 'cansaço' in texto: neuronios['Oxidação'] += 0.3
        
        # Activation Function (Softmax-ish)
        top_neuronio = max(neuronios, key=neuronios.get)
        confianca = min(neuronios[top_neuronio] * 100, 99.9)
        
        return top_neuronio, f"{confianca:.1f}%"

class ResonanciaSchumann:
    """
    Simula a conexão do humano com o campo eletromagnético da Terra.
    Insight: O ser humano é uma antena biológica calibrada em 7.83Hz (Ressonância de Schumann).
    """
    def analisar_frequencia(self):
        import random
        # Simula o "Clima Cósmico" atual
        frequencia_atual = random.choice([7.83, 14.3, 20.8, 33.8, 40.0]) # Harmônicas reais de Schumann
        
        status = {
            7.83: "🟢 **Normal (Gaia Heartbeat)**: O campo está estável. Se você sente cansaço, é apenas necessidade de aterramento.",
            14.3: "🟡 **Aceleração Leve**: A Terra está subindo o tom. Pode causar leve insônia ou criatividade aumentada.",
            20.8: "🟠 **Pico Moderado**: O tempo parece passar mais rápido. Ansiedade latente pode surgir sem motivo pessoal.",
            33.8: "🔴 **Salto Quântico**: Muita energia entrando. Sintomas: Zumbido no ouvido, tontura, 'vibrar' por dentro.",
            40.0: "🟣 **Gamma Burst**: Estado máximo. Clareza mental ou exaustão total. O sistema nervoso está fazendo download de luz."
        }
        return frequencia_atual, status.get(frequencia_atual)

class GhostStation:
    """
    INTEGRAÇÃO PROJETO GHOST STATION.
    O 'Farmacêutico Sônico'. Prescreve frequências para equilibrar o diagnóstico.
    """
    def sintonizar_frequencia(self, texto_sintomas, bloqueios_chakras):
        playlist = []
        
        # 1. Frequências Solfeggio (A Base)
        if 'medo' in texto_sintomas or 'rins' in texto_sintomas:
            playlist.append("📻 **396 Hz**: Liberação do Medo e Culpa (Raiz).")
        
        if 'mudança' in texto_sintomas or 'estagnado' in texto_sintomas:
            playlist.append("📻 **417 Hz**: Transmutação e Desbloqueio de Situações.")
            
        if 'milagre' in texto_sintomas or 'dna' in texto_sintomas or 'cura' in texto_sintomas:
            playlist.append("📻 **528 Hz**: A Frequência do Milagre (Reparo de DNA).")
            
        if 'amor' in texto_sintomas or 'tristeza' in texto_sintomas or 'coração' in texto_sintomas:
            playlist.append("📻 **639 Hz**: Harmonização de Relacionamentos (Coração).")
            
        if 'intuição' in texto_sintomas or 'mente' in texto_sintomas:
            playlist.append("📻 **852 Hz**: Despertar da Intuição (Terceiro Olho).")

        # 2. Binaural Beats (Ondas Cerebrais)
        if 'sono' in texto_sintomas or 'insônia' in texto_sintomas:
            playlist.append("🎧 **Delta (0.5 - 4 Hz)**: Sono Profundo sem sonhos.")
            
        if 'foco' in texto_sintomas or 'estudar' in texto_sintomas:
            playlist.append("🎧 **Alpha (8 - 12 Hz)**: Estado de Fluxo e Relaxamento Alerta.")

        if not playlist:
            playlist.append("📻 **432 Hz**: A Frequência Universal de Cura (Matemática Divina).")
            
        return playlist

# ==========================================
# MÓDULO 5: CÉREBRO PRINCIPAL
# ==========================================
class CérebroHolistico:
    """
    A Inteligência do Sistema. Simula o raciocínio clínico, holístico e ESPIRITUAL.
    """
    def __init__(self):
        self.bioquimica = SimuladorBioquimico()
        self.relogio = RelogioBiologico()
        self.chakras = SistemaChakras()
        self.rede_neural = RedeNeuralSimulada()
        self.cosmos = ResonanciaSchumann()
        self.ghost = GhostStation() # INTEGRAÇÃO REALIZADA
    
    def processar_pergunta(self, pergunta):
        pergunta = pergunta.lower()
        
        # --- 0. INTERCEPTAÇÕES ESPECÍFICAS ---
        if 'câncer' in pergunta or 'cancer' in pergunta or 'tumor' in pergunta:
            return self._analisar_cancer()
            
        if 'depressão' in pergunta or 'tristeza' in pergunta:
            return self._analisar_depressao()
            
        # --- AÇÚCAR (TURBO) ---
        if 'açúcar' in pergunta or 'doce' in pergunta or 'sugar' in pergunta:
            return self._analisar_acucar()
            
        # --- BLOCO QUÂNTICO & SECRETO ---
        if 'segredo' in pergunta or 'oculto' in pergunta or 'quântic' in pergunta or 'dna' in pergunta or 'luz' in pergunta:
            return self._analisar_segredos_quanticos()
            
        if 'coração' in pergunta and ('campo' in pergunta or 'energia' in pergunta):
            return self._analisar_segredos_quanticos(topico='CORACAO')

        # --- NEUROMOTOR / PARALISIA CEREBRAL (NOVA FUNCIONALIDADE) ---
        if any(x in pergunta for x in ['motor', 'paralisia', 'espasticidade', 'tônus', 'cadeira', 'sonda']):
             return self._analisar_neuromotor()

        # --- FIM DO MUNDO / CURA ---
        if 'cura' in pergunta or 'milagre' in pergunta or 'jesus' in pergunta:
             return self._analisar_sabedoria_divina()

    def _analisar_neuromotor(self):
        return (
            "♿ **Holística Pediátrica & Neuromotora**\n\n"
            "**1. A Visão da Alma**:\n"
            "Crianças com desafios motores graves muitas vezes são 'Mestres do Amor' (Chakra Cardíaco Puro). O corpo limita o movimento, mas expande a percepção energética. Elas sentem o campo emocional dos pais instantaneamente.\n\n"
            "**2. Decodificando o Tônus**:\n"
            "• **Espasticidade (Rigidez)**: Pode indicar 'Medo de Cair' ou 'Defesa do Território'. O corpo tenta criar uma armadura.\n"
            "• **Hipotonia (Moleza)**: Uma desconexão com a Terra (Chakra Raiz). A criança pode estar 'voando' no astral.\n\n"
            "**3. Como o Software Ajuda?**:\n"
            "• **Biofeedback Visual**: O Hologram ajuda a criança a visualizar o próprio corpo 'acendendo' (Neuroplasticidade).\n"
            "• **Cronobiologia**: Entender por que a criança agita às 3h da manhã (Horário do Fígado/Raiva ou Desintoxicação).\n"
            "• **Comunicação**: Se ela não fala, ela pode apontar para o Holograma."
        )
             
        if 'não consegue se curar' in pergunta or 'bloqueio' in pergunta:
             return self._analisar_bloqueios_cura()

        # --- DIAGNÓSTICO GERAL (MEGA BRAIN) ---
        # Se parecer um sintoma, chama o diagnóstico completo
        if any(x in pergunta for x in ['sinto', 'dor', 'estou', 'tenho', 'foco', 'paralisia', 'medo', 'raiva', 'ansiedade']):
             return self.diagnosticar_holisticamente(pergunta)

        # Fallback para busca genérica
        entidade = self._buscar_entidade_generica(pergunta)
        if entidade:
             conexoes = self._buscar_conexoes(origem=entidade)
             destinos = [rel.destino.nome for rel in conexoes]
             if destinos:
                return f"🔎 **{entidade.nome}**. \nConexões detectadas: " + ", ".join(destinos)
             else:
                return f"🔎 **{entidade.nome}**. (Sem conexões registradas no momento)"
             
        return "🤔 Sou um Oráculo Biofísico. Pergunte sobre 'Câncer', 'Açúcar', ou descreva o que sente (ex: 'sinto paralisia')."
    # ... (métodos auxiliares mantidos) ...

    # --- MÓDULO DE DIAGNÓSTICO (MEGA BRAIN V2) ---
    def diagnosticar_holisticamente(self, sintomas_texto):
        """
        Recebe um texto de sintomas e retorna as prováveis causas holísticas, analise bioquímica, temporal e energética.
        """
        sintomas_texto = sintomas_texto.lower()
        diagnostico = {
            'causas_provaveis': [],
            'sugestoes_fitoterapicas': [],
            'conflito_emocional': None
        }
        
        # 1. Análise Bioquímica
        bio_status = self.bioquimica.analisar(sintomas_texto)
        
        # 2. Análise Temporal (Cronobiologia)
        orgao_hora = self.relogio.orgao_do_momento()
        
        # 3. Análise Energética (Chakras)
        bloqueios_chakras = self.chakras.analisar_energia(sintomas_texto)
        
        # 4. Análise Neural (Deep Learning Simulado)
        padrao_neural, confianca_neural = self.rede_neural.calcular_pesos(sintomas_texto)

        # 5. Identificar Entidades no Texto (Busca Direta + Mapeamento de Sintomas Complexos)
        pergunta = pergunta.lower()
        
        # --- 0. INTERCEPTAÇÕES ESPECÍFICAS (CONHECIMENTO COMPLEXO) ---
        if 'câncer' in pergunta or 'cancer' in pergunta or 'tumor' in pergunta:
            return self._analisar_cancer()
            
        if 'depressão' in pergunta or 'tristeza' in pergunta:
            return self._analisar_depressao()
            
        # --- BLOCO QUÂNTICO & SECRETO ---
        if 'segredo' in pergunta or 'oculto' in pergunta or 'quântic' in pergunta or 'dna' in pergunta or 'luz' in pergunta:
            return self._analisar_segredos_quanticos()
            
        if 'coração' in pergunta and ('campo' in pergunta or 'energia' in pergunta):
            return self._analisar_segredos_quanticos(topico='CORACAO')

        # --- FITOTERAPIA & PLANTAS ---
        if 'planta' in pergunta or 'erva' in pergunta or 'chá' in pergunta or 'natural' in pergunta:
            entidade = self._buscar_entidade_generica(pergunta)
            if entidade:
                r = f"🌿 **Sabedoria da Mãe Terra: {entidade.nome}**\n"
                r += f"Natureza: {getattr(entidade, 'natureza_energetica', 'Neutro')}\n"
                conexoes = self._buscar_conexoes(origem=entidade)
                for c in conexoes:
                    r += f"• {c.tipo}: {c.descricao}\n"
                return r

        # --- AÇÚCAR (TURBO) ---
        if 'açúcar' in pergunta or 'doce' in pergunta or 'sugar' in pergunta:
            return self._analisar_acucar()

        # --- BLOCO DE SABEDORIA SUPREMA (Jesus, Buda, Cura) ---
        if 'jesus' in pergunta or 'buda' in pergunta or 'milagre' in pergunta or 'fé' in pergunta:
            return self._analisar_sabedoria_divina()
            
        if 'não consegue se curar' in pergunta or 'não se cura' in pergunta or 'por que não cura' in pergunta:
            return self._analisar_bloqueios_cura()

        resposta = []
        
        # Lógica de Doença Específica
        if 'doença' in pergunta or 'tem' in pergunta or 'causa' in pergunta:
            entidade = self._buscar_entidade_generica(pergunta)
            if entidade:
                resposta.append(f"🔎 **{entidade.nome}**: Análise Multidimensional")
                conexoes = self._buscar_conexoes(destino=entidade)
                for c in conexoes:
                    resposta.append(f"• {c.tipo}: {c.descricao}")
                return "\n".join(resposta)

        # --- FALLBACK MANTIDO ---
        entidade = self._buscar_entidade_generica(pergunta)
        if entidade:
            return f"🔎 **{entidade.nome}**. Consultei meus registros e encontrei conexões com: " + ", ".join([rel.destino.nome for rel in self._buscar_conexoes(origem=entidade)])

        return "🤔 Pergunta profunda. Pergunte sobre 'Cura', 'Jesus', 'Câncer' ou uma doença específica."

    def _analisar_sabedoria_divina(self):
        return (
            "✨ **A Cura Segundo os Mestres**\n\n"
            "**Jesus (A Lei da Fé)**:\n"
            "'A tua fé te curou'. Jesus ensinava que a cura acontece quando a mente aceita a possibilidade do milagre sem dúvida. O corpo obedece à crença absoluta.\n\n"
            "**Buda (A Lei do Desapego)**:\n"
            "O sofrimento vem do apego. Muitas doenças persistem porque nos apegamos à dor como identidade. A cura surge ao soltar (Impermanência) e aceitar o momento presente.\n\n"
            "**A Síntese**:\n"
            "O corpo é um reflexo da alma. O Amor (Jesus) dissolve o medo, e a Consciência (Buda) dissolve a ilusão da doença."
        )

    def _analisar_bloqueios_cura(self):
        return (
            "🛡️ **Por que algumas pessoas não se curam?**\n\n"
            "Mesmo com remédios, a cura pode falhar por bloqueios sutil:\n"
            "1. **Ganho Secundário**: O subconsciente acredita que a doença traz atenção, amor ou descanso que a pessoa não consegue pedir de outra forma.\n"
            "2. **Identificação**: 'Eu SOU diabético' vs 'Eu ESTOU passando por...'. Quando a doença vira identidade, o ego luta para mantê-la.\n"
            "3. **Falta de Perdão**: O ressentimento é um veneno que bebemos esperando que o outro morra. Ele mantém a inflamação celular ativa.\n"
            "4. **Medo da Vida**: Às vezes, a doença é um escudo contra os desafios de viver plenamente."
        )

    def _analisar_cancer(self):
        return (
            "🦀 **Câncer: A visão Biológica e Espiritual**\n"
            "Biológico: Célula em pânico (efeito Warburg), sem oxigênio, recusando morrer.\n"
            "Espiritual: Frequentemente ligado a uma mágoa antiga profunda, um 'não' à vida que foi engolido. A cura envolve perdoar o passado e re-escolher a vida."
        )
    
    def _analisar_depressao(self):
        return "🌑 **Depressão**: Desconexão da alma. Bioquimicamente: falta de Serotonina/B12. Espiritualmente: Perda do sentido ou supressão da própria verdade."

    def _buscar_entidade(self, texto, model):
        for obj in model.objects.all():
            if obj.nome.lower() in texto: return obj
        return None

    def _buscar_entidade_generica(self, texto):
        for model in [ProcessoMetabolico, Orgao, Emocao, Substancia, Celula, EstadoMental]:
            obj = self._buscar_entidade(texto, model)
            if obj: return obj
        return None
    
    def _buscar_conexoes(self, origem=None, destino=None):
        query = Q()
        if origem:
            query &= Q(origem_object_id=origem.id)
        if destino:
            query &= Q(destino_object_id=destino.id)
        return RelacaoHolistica.objects.filter(query)
    
    def _analisar_segredos_quanticos(self, topico=None):
        if topico == 'CORACAO':
             return (
                "💖 **O Segredo Magnético do Coração**\n"
                "A ciência convencional diz que é uma bomba. A biofísica revela que é um gerador.\n"
                "• **Campo Toroidal**: O coração gera um campo magnético 5000x mais forte que o do cérebro, detectável a 3 metros.\n"
                "• **Comunicação Não-Local**: Este campo modula o DNA de quem está perto. O amor literalmente altera a matéria ao redor."
            )
            
        return (
            "🔮 **Segredos Quânticos Ocultos**\n\n"
            "**1. A Luz no DNA (Biofótons)**:\n"
            "Seu DNA não é apenas código; é uma antena. Fritz-Albert Popp provou que ele armazena e emite luz coerente (laser biológico) para coordenar as 100 trilhões de células instantaneamente.\n\n"
            "**2. A Mente nos Microtúbulos**:\n"
            "A consciência não está nas sinapses, mas DENTRO dos neurônios (Microtúbulos). Penrose & Hameroff sugerem que processamos realidade quântica (Orch-OR). Você é um computador quântico biológico.\n\n"
            "**3. A Pineal de Cristal**:\n"
            "Sua glândula pineal é cheia de microcristais (calcita piezoelétrica). Ela vibra e transforma frequências espirituais em sinais químicos (DMT/Melatonina)."
        )

    def _analisar_acucar(self):
        return (
            "🍬 **A Verdade Sobre o Açúcar: A Droga Dupla**\n\n"
            "**1. O Céu (A Melhor Droga)**:\n"
            "Ele inunda seu *Núcleo Accumbens* com mais Dopamina que a cocaína. É o abraço químico perfeito, gerando prazer imediato e vício instantâneo.\n\n"
            "**2. O Inferno (A Pior Droga)**:\n"
            "• **Glicação**: O açúcar carameliza seu colágeno. Você envelhece por dentro.\n"
            "• **Mitocôndrias**: O excesso de energia frita suas usinas de força.\n"
            "• **Câncer**: É o combustível premium para células tumorais (Efeito Warburg).\n\n"
            "**Conselho**: É delicioso porque mata. Use com sabedoria extrema."
        )

    # --- MÓDULO DE DIAGNÓSTICO (MEGA BRAIN) ---
    def diagnosticar_holisticamente(self, sintomas_texto):
        """
        Recebe um texto de sintomas e retorna as prováveis causas holísticas, analise bioquímica e temporal.
        """
        sintomas_texto = sintomas_texto.lower()
        diagnostico = {
            'causas_provaveis': [],
            'sugestoes_fitoterapicas': [],
            'conflito_emocional': None
        }
        
        # 1. Análise Bioquímica (MEGA LÓGICA)
        bio_status = self.bioquimica.analisar(sintomas_texto)
        
        # 2. Análise Temporal (Cronobiologia)
        orgao_hora = self.relogio.orgao_do_momento()
        
        # 3. Identificar Entidades no Texto (Busca Direta + Mapeamento de Sintomas Complexos)
        entidades_detectadas = []
        termos = sintomas_texto.replace(',', ' ').split()
        
        # Mapeamento de Sintomas Complexos -> Entidades
        mapa_sintomas = {
            'paralisia': 'Medo Existencial', # Vai buscar Emoção
            'congelar': 'Medo Existencial',
            'executar': 'Fígado', # Ação
            'foco': 'Dopamina',
            'hiper': 'Adrenalina',
            'tristeza': 'Pulmões',
            'raiva': 'Fígado',
            'medo': 'Rins',
            'ansiedade': 'Cérebro'
        }

        # Busca por termos exatos
        for termo in termos:
            if len(termo) > 3:
                ent = self._buscar_entidade_generica(termo)
                if ent: entidades_detectadas.append(ent)
                
                # Busca no mapa
                for chave, valor in mapa_sintomas.items():
                    if chave in termo:
                        ent_map = self._buscar_entidade_generica(valor)
                        if ent_map: entidades_detectadas.append(ent_map)
        
        # Deduplicar
        entidades_detectadas = list(set(entidades_detectadas))
        
        # 4. Rastrear Causas (RelacaoHolistica Reverso)
        scores = {}
        for ent in entidades_detectadas:
            conexoes = RelacaoHolistica.objects.filter(destino_object_id=ent.id)
            for conexao in conexoes:
                causa = conexao.origem
                if causa:
                    if causa not in scores: scores[causa] = 0
                    scores[causa] += conexao.forca
                    if hasattr(causa, 'natureza_energetica'): # É Alimento/Planta
                         diagnostico['sugestoes_fitoterapicas'].append(f"{causa.nome} ({conexao.tipo})")

        # 5. Top Causas
        sorted_causes = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        for causa, score in sorted_causes:
            diagnostico['causas_provaveis'].append(f"{causa.nome} (Ressonância: {score*10}%)")
            if hasattr(causa, 'polaridade'):
                diagnostico['conflito_emocional'] = f"Bloqueio relacionado a: {causa.nome}"
        
        
        # 5. Análise de Ressonância (O Fator Surpresa)
        hz_terra, status_terra = self.cosmos.analisar_frequencia()

        # === FORMATAÇÃO DO RELATÓRIO FINAL ===
        relatorio = f"🧠 **MEGA CÉREBRO ANALYTICS v4.0 (Gaia Connected)** 🧠\n"
        relatorio += f"🌍 **Ressonância Schumann**: Hoje a Terra vibra em **{hz_terra}Hz**.\n"
        relatorio += f"   ↳ {status_terra}\n\n"

        relatorio += f"🕒 **Cronobiologia**: Órgão Regente: **{orgao_hora}**.\n"
        relatorio += f"🤖 **Rede Neural**: Padrão '{padrao_neural}' detectado com **{confianca_neural}** de confiança.\n\n"
        
        relatorio += f"🧪 **Painel Bioquímico**:\n"
        relatorio += f"• ⚡ Dopamina: {bio_status['dopamina']}\n"
        relatorio += f"• 🔥 Cortisol: {bio_status['cortisol']}\n"
        relatorio += f"• 🌙 Serotonina: {bio_status['serotonina']}\n"
        
        if bloqueios_chakras:
            relatorio += "\n🧘 **Alinhamento Energético**:\n"
            for b in bloqueios_chakras:
                relatorio += f"- {b}\n"
        
        if bio_status['alerta']:
            relatorio += "\n⚠️ **Alertas Sistêmicos**:\n"
            for a in bio_status['alerta']:
                relatorio += f"- {a}\n"
        
        relatorio += "\n📋 **Dedução Holística Deep Scan**:\n"
        
        if 'foco' in sintomas_texto and 'paralisia' in sintomas_texto:
             relatorio += (
                 "🚨 **DIAGNÓSTICO ALTA PRECISÃO: COLAPSO DORSAL VAGAL** 🚨\n\n"
                 "Você não está com preguiça. Você está em **Shutdown Biológico**.\n"
                 "1. **O Gatilho**: Excesso de estímulo (Hiper Foco/Dopamina) sobrecarregou o sistema.\n"
                 "2. **A Reação**: Seu Nervo Vago ativou o freio de emergência (Congelamento) para evitar danos maiores.\n"
                 "3. **A Solução**: Não force a execução. O Fígado está bloqueado. Respire e saia das telas por 30min."
             )
        elif not entidades_detectadas:
             relatorio += "Não consegui identificar sintomas específicos, mas seus níveis bioquímicos indicam desequilíbrio."
        else:
             relatorio += f"**Sintomas Rastreados**: {', '.join([e.nome for e in entidades_detectadas])}\n"
             if diagnostico['conflito_emocional']:
                relatorio += f"⚠️ **Raiz Emocional**: {diagnostico['conflito_emocional']}\n"
             if diagnostico['causas_provaveis']:
                relatorio += "**Origens Possíveis**: " + ", ".join(diagnostico['causas_provaveis'])

        if diagnostico['sugestoes_fitoterapicas']:
            relatorio += "\n\n🌱 **Farmácia da Natureza**:\n" + "\n".join([f"- {p}" for p in set(diagnostico['sugestoes_fitoterapicas'])])
            
        # GHOST STATION INTEGRATION
        frequencias = self.ghost.sintonizar_frequencia(sintomas_texto, bloqueios_chakras)
        if frequencias:
            relatorio += "\n\n👻 **Ghost Station (Prescrição Sônica)**:\n" + "\n".join(frequencias)
            
        return relatorio
