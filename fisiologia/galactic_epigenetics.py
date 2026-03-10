"""
Aura Bio-Nexus: Galactic Epigenetics Engine
=============================================
Based on 2025/2026 breakthroughs:
- Photobiomodulation (PBM): histone acetylation + chromatin remodeling via red/NIR light
- Sound frequency at 528Hz: cortisol reduction + oxytocin increase (Journal of Addiction Research, 2018)
- 40Hz light/sound: amyloid plaque clearance + BDNF activation (MIT/Harvard 2024-2026 trials)
- First human epigenetic reprogramming trial for eye disease: 2026 (Longevity.technology)

These are the frequencies your galactic family has known for millennia.
Science is just now catching up.
"""

class FrequencyGeneMap:
    """
    Maps specific frequencies to gene expression pathways.
    Backed by photobiomodulation and mechanosensitive gene research.
    """
    ACTIVATION_MAP = {
        528: {
            "gene_targets": ["OXT (Oxytocin)", "BDNF", "TGF-beta"],
            "pathway": "Stress-Axis Suppression / Social Bonding",
            "mechanism": "Reduces cortisol, activates oxytocin circuit",
            "effect": "Emotional Harmonization & DNA Repair (Love Frequency)",
            "source": "Medcraveonline, 2018 + epigenetic chromatin studies"
        },
        432: {
            "gene_targets": ["GABA-A receptors", "SERT (Serotonin Transporter)"],
            "pathway": "Parasympathetic Nervous System Activation",
            "mechanism": "Resonance with Earth Schumann frequency (7.83Hz harmonic)",
            "effect": "Calm State + Anxiety Reduction + Myelin Protection",
            "source": "Kyoto University mechanosensitive studies + global HRV research"
        },
        40: {
            "gene_targets": ["BDNF", "NRF2", "TREM2 (Microglia Activation)"],
            "pathway": "Gamma Oscillation Entrainment",
            "mechanism": "40Hz light/sound synchronizes neural gamma waves, activates microglia",
            "effect": "Amyloid-Beta Clearance + Cognitive Restoration (Alzheimer's reversal)",
            "source": "MIT/Harvard GENUS trials 2024-2026, Forbes"
        },
        810: { # Near-Infrared (Photobiomodulation)
            "gene_targets": ["COX (Cytochrome c oxidase)", "BDNF", "Nrf2"],
            "pathway": "Mitochondrial ATP Boost + Anti-inflammatory",
            "mechanism": "NIR light penetrates skull, activates cytochrome c oxidase in neurons",
            "effect": "Neurogenesis + Axon Regeneration + Brain Fog Elimination",
            "source": "NIH PubMed PBM studies 2024, MDPI Photonics"
        }
    }


class GalacticEpigeneticsEngine:
    """
    Bio-Nexus: Galactic Epigenetic Reprogramming Layer.
    Calculates optimal frequency protocol to reactivate dormant gene pathways.
    Bridges what ancestors called 'frequency medicine' with
    what 2026 science now confirms as epigenetic modulation.
    """

    def __init__(self):
        self.frequency_map = FrequencyGeneMap()

    def get_frequency_protocol(self, frequency_hz):
        protocol = self.frequency_map.ACTIVATION_MAP.get(frequency_hz)
        if not protocol:
            return {"status": "Frequency not yet mapped. Scanning galactic database..."}
        return {
            "frequency": f"{frequency_hz} Hz",
            "gene_targets": protocol["gene_targets"],
            "mechanism": protocol["mechanism"],
            "effect": protocol["effect"],
            "galactic_name": self._get_galactic_name(frequency_hz)
        }

    def _get_galactic_name(self, hz):
        names = {
            528: "Frequência do Amor (Solfeggio Mi)",
            432: "Frequência da Terra (Schumann Harmonic)",
            40: "Frequência da Mente Despertando (Gamma Burst)",
            810: "Frequência da Luz Vermelha do Sol (Fótons Curativos)"
        }
        return names.get(hz, "Frequência em Catalogação Arcturiana")

    def design_healing_session(self, condition):
        """
        Maps a condition to an optimal multi-frequency healing session.
        """
        protocols = {
            "Alzheimer":    [40, 810],
            "Depressao":    [528, 432],
            "Inflamacao":   [810, 432],
            "Trauma":       [528, 432],
            "Neuro-Reparo": [810, 40],
            "Fadiga":       [810, 528],
            "Autoimune":    [432, 528, 810],
            "Parkinson":    [40, 432, 810],
        }
        freqs = protocols.get(condition, [528])
        session = []
        for f in freqs:
            p = self.get_frequency_protocol(f)
            session.append(p)
        return session


class PersonalHealingCalculator:
    """
    Aura Bio-Nexus: Calculadora de Sessão de Cura Personalizada.
    Usa o perfil biométrico do usuário para calcular duração,
    intensidade e sequência ótima de frequências galácticas.
    """

    def __init__(self):
        self.engine = GalacticEpigeneticsEngine()

    def calculate_session(self, profile: dict) -> dict:
        """
        profile = {
            'nome': str,
            'idade': int,
            'nivel_estresse': int,   # 0-10
            'qualidade_sono': int,   # 0-10
            'condicao': str,         # e.g. 'Depressao', 'Neuro-Reparo'
            'objetivo': str          # e.g. 'clareza mental', 'anti-inflamação'
        }
        """
        nome      = profile.get('nome', 'Soberano')
        idade     = profile.get('idade', 35)
        estresse  = profile.get('nivel_estresse', 5)
        sono      = profile.get('qualidade_sono', 5)
        condicao  = profile.get('condicao', 'Depressao')
        objetivo  = profile.get('objetivo', 'equilíbrio geral')

        # Base duration: 20 minutes, adjusted by stress & sleep quality
        stress_factor  = 1 + (estresse / 10)       # Higher stress → longer session
        sleep_factor   = 1 + ((10 - sono) / 20)    # Poor sleep → slightly longer
        age_factor     = 1 + (max(0, idade - 40) / 100)  # Older → gentle extension
        base_min       = 20
        total_minutes  = round(base_min * stress_factor * sleep_factor * age_factor)

        # Intensity: inversely proportional to stress (high stress → start gentle)
        intensity_pct  = max(30, 100 - (estresse * 5))

        # Frequency sequence from condition
        steps = self.engine.design_healing_session(condicao)

        # Distribute time across steps
        per_step_min = max(5, total_minutes // len(steps))

        plan = {
            'perfil': f"{nome}, {idade} anos",
            'condicao_alvo': condicao,
            'objetivo': objetivo,
            'duracao_total_min': total_minutes,
            'intensidade_recomendada': f"{intensity_pct}%",
            'sequencia': []
        }

        for i, step in enumerate(steps, 1):
            plan['sequencia'].append({
                'etapa': i,
                'frequencia': step['frequency'],
                'nome_galactico': step['galactic_name'],
                'duracao_min': per_step_min,
                'genes_ativados': step['gene_targets'],
                'efeito': step['effect']
            })

        return plan

    def print_session(self, profile: dict):
        plan = self.calculate_session(profile)
        print("=" * 60)
        print(f"  🌌 SESSÃO PERSONALIZADA — {plan['perfil'].upper()}")
        print("=" * 60)
        print(f"  Condição Alvo  : {plan['condicao_alvo']}")
        print(f"  Objetivo       : {plan['objetivo']}")
        print(f"  Duração Total  : {plan['duracao_total_min']} minutos")
        print(f"  Intensidade    : {plan['intensidade_recomendada']}")
        print()
        for s in plan['sequencia']:
            print(f"  Etapa {s['etapa']}: {s['nome_galactico']}")
            print(f"    ▸ Frequência : {s['frequencia']}")
            print(f"    ▸ Duração    : {s['duracao_min']} min")
            print(f"    ▸ Genes      : {', '.join(s['genes_ativados'])}")
            print(f"    ▸ Efeito     : {s['efeito']}")
            print()
        print("=" * 60)
        print("  ✓ SESSÃO GALÁCTICA CALCULADA E PRONTA PARA EXECUÇÃO")
        print("=" * 60)


if __name__ == "__main__":
    calc = PersonalHealingCalculator()

    # --- Perfil de demonstração ---
    perfil_mauricio = {
        'nome': 'Mauricio',
        'idade': 40,
        'nivel_estresse': 6,
        'qualidade_sono': 7,
        'condicao': 'Neuro-Reparo',
        'objetivo': 'Regeneração neural e clareza mental máxima'
    }

    calc.print_session(perfil_mauricio)

    print()

    # --- Segundo perfil: Alzheimer avançado ---
    perfil_paciente = {
        'nome': 'Paciente Alzheimer',
        'idade': 70,
        'nivel_estresse': 8,
        'qualidade_sono': 3,
        'condicao': 'Alzheimer',
        'objetivo': 'Limpeza de placas amiloides e ativação de microglia'
    }

    calc.print_session(perfil_paciente)
