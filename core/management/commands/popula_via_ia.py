
import os
import json
import google.generativeai as genai
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from anatomia.models import Orgao, SistemaCorporal
from psicologia.models import Emocao
from core.models import RelacaoHolistica

# Chave API detectada e validada
API_KEY = "AIzaSyBREWGg-uOUss7bZIoK0xqBU5svqvyCX6Y" 

class Command(BaseCommand):
    help = 'Usa IA (Gemini 2.5 Pro) para popular o banco com relacionamentos holísticos profundos'

    def handle(self, *args, **kwargs):
        self.stdout.write("🧠 Conectando ao Omni Brain (Gemini 2.5 Pro)...")
        
        # Limpeza
        self.stdout.write("🧹 Limpando dados antigos para nova injeção...")
        RelacaoHolistica.objects.all().delete()
        Orgao.objects.all().delete()
        Emocao.objects.all().delete()
        SistemaCorporal.objects.all().delete()

        genai.configure(api_key=API_KEY)
        # Usando o modelo mais poderoso disponível na chave do usuário
        model = genai.GenerativeModel('gemini-2.5-pro')

        prompt = """
        Atue como o maior especialista mundial em Medicina Integrativa, unindo a precisão da Anatomia Gray com a sabedoria da MTC (Medicina Tradicional Chinesa), Ayurveda e Nova Medicina Germânica.
        
        Gere um objeto JSON contendo uma lista de 40 Relações Holísticas profundas e não-óbvias.
        
        REGRAS CRÍTICAS:
        1. Responda APENAS o JSON. Sem markdown (```json), sem introdução.
        2. Seja específico e técnico nas descrições.
        
        Estrutura do JSON:
        {
            "relations": [
                {
                    "emotion": "Nome da Emoção ou Conflito Biológico",
                    "organ": "Nome do Órgão ou Tecido Específico",
                    "organ_system": "Sistema Anatômico",
                    "relation_type": "Uma destas: CAUSA_FISICA, INIBE, ESTIMULA, AGRAVA, SIMBOLIZA, CURA, CORRELACAO",
                    "description": "Explicação densa conectando a emoção à patologia ou função do órgão.",
                    "strength": Inteiro de 1 a 10
                }
            ]
        }
        """

        try:
            self.stdout.write("⏳ Gerando conhecimento (isso pode levar alguns segundos)...")
            response = model.generate_content(prompt)
            
            # Limpeza robusta do response
            clean_text = response.text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            
            data = json.loads(clean_text)
            
            self.stdout.write(f"📥 Recebido {len(data['relations'])} unidades de sabedoria. Injetando...")
            
            count = 0
            for item in data['relations']:
                # 1. Cria/Pega Sistema
                sistema, _ = SistemaCorporal.objects.get_or_create(nome=item.get('organ_system', 'Sistema Integrado'))
                
                # 2. Cria/Pega Órgão
                orgao, _ = Orgao.objects.get_or_create(
                    nome=item['organ'],
                    defaults={'sistema': sistema, 'funcao_biologica': 'Processado via Gemini 2.5 Pro'}
                )
                
                # 3. Cria/Pega Emoção
                emocao, _ = Emocao.objects.get_or_create(
                    nome=item['emotion'],
                    defaults={'polaridade': 'NEUTRA'} # Deixa neutra se não especificado
                )
                
                # 4. Cria Relação
                ct_origem = ContentType.objects.get_for_model(emocao)
                ct_destino = ContentType.objects.get_for_model(orgao)
                
                Relacao, created = RelacaoHolistica.objects.get_or_create(
                    origem_content_type=ct_origem,
                    origem_object_id=emocao.id,
                    destino_content_type=ct_destino,
                    destino_object_id=orgao.id,
                    defaults={
                        'tipo': item['relation_type'],
                        'descricao': item['description'],
                        'forca': item['strength'],
                        'fonte': 'Gemini 2.5 Pro'
                    }
                )
                
                if created:
                    count += 1
                    self.stdout.write(f"   [+] {emocao} -> {orgao}")

            self.stdout.write(self.style.SUCCESS(f"✅ Sucesso Absoluto! {count} conexões de alta fidelidade criadas."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro Fatal na IA: {str(e)}"))
