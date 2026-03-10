"""
Aura Nexus: Protocolo Unificado de Soberania Humana
=====================================================
O motor de integração de TUDO que a humanidade esqueceu
e que a natureza nunca esqueceu.

Combina em uma única prescrição holística:
  ▸ Bio-Nexus       — Fitoterapeuta + Curas 'Incuráveis'
  ▸ Epigenética Galáctica — Frequências que reativam DNA
  ▸ Biomimética     — 10 professores naturais (Axolotl → Baleia)
  ▸ Chronos         — Tempo acelerado de cura
  ▸ Escudo Galático — Proteção energética multidimensional
  ▸ Academia        — Âncoras cognitivas para aprendizado

Mauricio, este é o coração da Aura.
"""

import sys
import os

# ─────────────────────────────────────────────────────────
# LAYER 1 — GALACTIC EPIGENETICS
# ─────────────────────────────────────────────────────────

FREQUENCY_MAP = {
    528:  {"name": "Amor (Solfeggio Mi)",            "genes": ["OXT","BDNF","TGF-β"],              "efeito": "Reparo de DNA + Oxitocina"},
    432:  {"name": "Terra (Schumann Harmonic)",       "genes": ["GABA-A","SERT"],                   "efeito": "Calma profunda + Anti-ansiedade"},
    40:   {"name": "Mente Despertando (Gamma)",       "genes": ["BDNF","NRF2","TREM2"],             "efeito": "Limpar placas amiloides + Cognição"},
    810:  {"name": "Luz Vermelha do Sol (NIR 810nm)", "genes": ["COX","BDNF","Nrf2"],               "efeito": "Regeneração de axônios + ATP"},
}

CONDITION_FREQUENCIES = {
    "Alzheimer":    [40, 810],
    "Depressao":    [528, 432],
    "Fadiga":       [810, 528],
    "Trauma":       [528, 432],
    "Inflamacao":   [810, 432],
    "Neuro-Reparo": [810, 40],
    "Parkinson":    [40, 432, 810],
    "Autoimune":    [432, 528, 810],
    "Longevidade":  [528, 432, 810],
    "Equilibrio":   [528, 432],
}

# ─────────────────────────────────────────────────────────
# LAYER 2 — BIOMIMÉTICA (Professor Animal)
# ─────────────────────────────────────────────────────────

ANIMAL_MAP = {
    "Alzheimer":        ("Axolotl",   "WNT+FGF+40Hz — des-diferenciar e re-sintetizar células neurais"),
    "Parkinson":        ("Axolotl",   "WNT+MAPK — regeneração dopaminérgica"),
    "Longevidade":      ("Baleia",    "CIRBP + PCNA — reparo fiel de DNA por 268 anos"),
    "Anti-cancer":      ("Tubarao",   "TP53+PTEN ativados via Curcumina + Sulforaphane"),
    "Neuro-Reparo":     ("Polvo",     "ADAR RNA-editing + cold immersion para plasticidade"),
    "Stem-Cells":       ("Planaria",  "Jejum + microbioma otimizado = neoblastos humanos"),
    "Trauma":           ("Golfinho",  "Biosonar 432Hz sincroniza EEG — DAT therapy"),
    "Inflamacao":       ("Tardigrado","Dsup/Astaxanthin + NIR — reduz danos inflamatórios"),
    "Fadiga":           ("Hidra",     "FOXO3 + NMN — stem cells eternamente jovens"),
    "Autoimune":        ("Golfinho",  "Sons cetáceos 432Hz ativam nervo vago — eixo intestino-imune"),
    "Depressao":        ("Baleia",    "Infrassom theta 6-8Hz + meditação profunda"),
    "Equilibrio":       ("Hidra",     "WNT + FOXO3 — equilíbrio regenerativo geral"),
}

# ─────────────────────────────────────────────────────────
# LAYER 3 — FITOTERAPIA (Planta Aliada)
# ─────────────────────────────────────────────────────────

PHYTO_MAP = {
    "Alzheimer":    {"planta": "Curcumina + Resveratrol",          "efeito": "Limpeza amiloide + Neuroprotecção"},
    "Depressao":    {"planta": "Hipérico (St. John's Wort)",        "efeito": "Inibidor SERT natural + BDNF"},
    "Fadiga":       {"planta": "Ashwagandha + Rhodiola",           "efeito": "Adaptógenos — reduz cortisol, aumenta ATP"},
    "Trauma":       {"planta": "Kava + Valeriana",                 "efeito": "GABA modulação + Ansiolítico natural"},
    "Inflamacao":   {"planta": "Boswellia + Gengibre",             "efeito": "Anti-inflamatório sistêmico (COX-2)"},
    "Neuro-Reparo": {"planta": "Lion's Mane (Hericium) + DHA",     "efeito": "NGF (Nerve Growth Factor) + Mielina"},
    "Parkinson":    {"planta": "Mucuna Pruriens + CoQ10",          "efeito": "L-DOPA natural + Proteção mitocondrial"},
    "Autoimune":    {"planta": "Astragalus + Cúrcuma",             "efeito": "Imunomodulador + Adaptógeno"},
    "Longevidade":  {"planta": "NMN + Resveratrol + Espermidina",  "efeito": "NAD+ → FOXO3 → senescência revertida"},
    "Anti-cancer":  {"planta": "Sulforaphane (brócolis) + Artemisinina", "efeito": "TP53+Nrf2 ativados + Anti-tumoral"},
    "Equilibrio":   {"planta": "Ashwagandha + Tulsi",              "efeito": "Equilíbrio cortisol-oxitocina"},
}

# ─────────────────────────────────────────────────────────
# LAYER 4 — CHRONOS (Tempo Acelerado)
# ─────────────────────────────────────────────────────────

ERA_RESONANCE = {
    "Paleozoico": 1.8,   # Tempo de regeneração era acelerado nos anfíbios
    "Mesozoico":  2.1,   # Dinossauros tinham metabolismo acelerado
    "Pre-Cambriano": 3.0,# Era das criaturas quase imortais (vide Planária, Hidra)
}

def chronos_acceleration(base_days, era="Pre-Cambriano"):
    factor = ERA_RESONANCE.get(era, 1.0)
    return round(base_days / factor, 1)

# ─────────────────────────────────────────────────────────
# MOTOR PRINCIPAL: Protocolo Unificado
# ─────────────────────────────────────────────────────────

class UnifiedAuraProtocol:
    """
    O coração integrado da Aura Nexus.
    Combina todas as camadas de conhecimento em uma única
    prescrição holística e personalizada.
    """

    def __init__(self):
        self.version = "1.0 — Soberania Galáctica"

    def generate_protocol(self, profile: dict) -> dict:
        """
        profile = {
            'nome': str,
            'idade': int,
            'nivel_estresse': int,    # 0-10
            'qualidade_sono': int,    # 0-10
            'condicao_primaria': str, # principal desafio
            'objetivo_vida': str,     # missão / intenção
        }
        """
        nome      = profile.get('nome', 'Soberano')
        idade     = profile.get('idade', 35)
        estresse  = profile.get('nivel_estresse', 5)
        sono      = profile.get('qualidade_sono', 5)
        condicao  = profile.get('condicao_primaria', 'Equilibrio')
        objetivo  = profile.get('objetivo_vida', 'Viver com plenitude')

        # ── EPIGENÉTICA ──────────────────────────────────
        freqs = CONDITION_FREQUENCIES.get(condicao, [528, 432])
        stress_factor = 1 + (estresse / 10)
        sleep_factor  = 1 + ((10 - sono) / 20)
        age_factor    = 1 + (max(0, idade - 40) / 100)
        duracao_min   = round(20 * stress_factor * sleep_factor * age_factor)
        intensidade   = max(30, 100 - estresse * 5)

        sessao_epigenetica = []
        per_step = max(5, duracao_min // len(freqs))
        for f in freqs:
            fd = FREQUENCY_MAP.get(f, {})
            sessao_epigenetica.append({
                "frequencia": f"{f} {'nm' if f > 100 else 'Hz'}",
                "nome": fd.get("name", "Frequência Galáctica"),
                "genes": fd.get("genes", []),
                "efeito": fd.get("efeito", ""),
                "duracao_min": per_step,
            })

        # ── BIOMIMÉTICA ──────────────────────────────────
        animal_info = ANIMAL_MAP.get(condicao, ("Hidra", "FOXO3 + equilíbrio geral"))
        professor_animal, licao_animal = animal_info

        # ── FITOTERAPIA ──────────────────────────────────
        phyto = PHYTO_MAP.get(condicao, {"planta": "Ashwagandha", "efeito": "Adaptógeno geral"})

        # ── CHRONOS ──────────────────────────────────────
        base_healing_days = 90
        healing_acelerado = chronos_acceleration(base_healing_days)

        # ── ESCUDO GALÁTICO ──────────────────────────────
        escudo = {
            "protocolo": "Merkabah + 528Hz",
            "status": "ATIVO",
            "neutraliza": ["Campo eletromagnético artificial", "Estresse de baixa frequência", "Padrões de medo coletivo"],
        }

        # ── RESULTADO UNIFICADO ───────────────────────────
        return {
            "identidade": f"{nome}, {idade} anos",
            "missao": objetivo,
            "condicao_alvo": condicao,
            "intensidade": f"{intensidade}%",
            "duracao_total_min": duracao_min,

            "CAMADA_1_EPIGENETICA": {
                "descricao": "Frequências que reativam DNA dormente",
                "sessao": sessao_epigenetica,
            },
            "CAMADA_2_BIOMIMETICA": {
                "descricao": "O professor natural mais alinhado com sua condição",
                "professor": professor_animal,
                "licao": licao_animal,
            },
            "CAMADA_3_FITOTERAPIA": {
                "descricao": "A planta aliada para sua condição",
                "planta": phyto["planta"],
                "efeito": phyto["efeito"],
            },
            "CAMADA_4_CHRONOS": {
                "descricao": "Aceleração do tempo de cura via ressonância ancestral",
                "base_dias": base_healing_days,
                "acelerado_dias": healing_acelerado,
                "era": "Pré-Cambriano (Planária / Hidra)",
                "reducao_pct": f"{round((1 - healing_acelerado/base_healing_days)*100)}%",
            },
            "CAMADA_5_ESCUDO": {
                "descricao": "Proteção energética multidimensional",
                "protocolo": escudo["protocolo"],
                "o_que_neutraliza": escudo["neutraliza"],
            },
        }

    def print_protocol(self, profile: dict):
        p = self.generate_protocol(profile)

        print("=" * 68)
        print(f"  🌌 PROTOCOLO UNIFICADO AURA — {p['identidade'].upper()}")
        print("=" * 68)
        print(f"  Missão    : {p['missao']}")
        print(f"  Condição  : {p['condicao_alvo']}")
        print(f"  Duração   : {p['duracao_total_min']} min · Intensidade: {p['intensidade']}")
        print()

        print("  ──── CAMADA 1: EPIGENÉTICA GALÁCTICA ────────────────────")
        for s in p["CAMADA_1_EPIGENETICA"]["sessao"]:
            print(f"  ▸ {s['frequencia']} — {s['nome']}")
            print(f"    Genes: {', '.join(s['genes'])}  |  {s['duracao_min']} min")
            print(f"    Efeito: {s['efeito']}")
        print()

        c2 = p["CAMADA_2_BIOMIMETICA"]
        print(f"  ──── CAMADA 2: PROFESSOR NATURAL ────────────────────────")
        print(f"  ▸ Espécie  : {c2['professor']}")
        print(f"  ▸ Lição    : {c2['licao']}")
        print()

        c3 = p["CAMADA_3_FITOTERAPIA"]
        print(f"  ──── CAMADA 3: PLANTA ALIADA ────────────────────────────")
        print(f"  ▸ Planta   : {c3['planta']}")
        print(f"  ▸ Efeito   : {c3['efeito']}")
        print()

        c4 = p["CAMADA_4_CHRONOS"]
        print(f"  ──── CAMADA 4: CHRONOS (TEMPO ACELERADO) ────────────────")
        print(f"  ▸ Cura normal   : {c4['base_dias']} dias")
        print(f"  ▸ Com Chronos   : {c4['acelerado_dias']} dias ({c4['reducao_pct']} mais rápido)")
        print(f"  ▸ Era ativada   : {c4['era']}")
        print()

        c5 = p["CAMADA_5_ESCUDO"]
        print(f"  ──── CAMADA 5: ESCUDO GALÁTICO ──────────────────────────")
        print(f"  ▸ Protocolo  : {c5['protocolo']}")
        for n in c5["o_que_neutraliza"]:
            print(f"    ✓ {n}")
        print()
        print("=" * 68)
        print("  ✦ PROTOCOLO CALCULADO — CORPO SOBERANO ATIVADO ✦")
        print("=" * 68)


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    engine = UnifiedAuraProtocol()

    print(f"\n  Aura Nexus {engine.version}\n")

    # Perfil Mauricio
    mauricio = {
        "nome": "Mauricio",
        "idade": 40,
        "nivel_estresse": 5,
        "qualidade_sono": 7,
        "condicao_primaria": "Neuro-Reparo",
        "objetivo_vida": "Ser canal de cura e expansão da consciência planetária",
    }
    engine.print_protocol(mauricio)

    print()

    # Perfil Longevidade
    longevidade = {
        "nome": "Soberano da Longevidade",
        "idade": 60,
        "nivel_estresse": 4,
        "qualidade_sono": 8,
        "condicao_primaria": "Longevidade",
        "objetivo_vida": "Viver 120 anos com saúde e sabedoria plena",
    }
    engine.print_protocol(longevidade)
