
import os
import chromadb
from django.core.management.base import BaseCommand
from anatomia.models import Orgao

class Command(BaseCommand):
    help = 'HEALER-BOT: Enriquece dados médicos com sabedoria holística (PsicoCodex).'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🏥 INICIANDO PROTOCOLO DE CURA (Codex -> Holístico)...'))

        CODEX_MEMORY_PATH = r"c:\Users\Mauricio\Desktop\codex-IA\.codex_memory"
        
        try:
            client = chromadb.PersistentClient(path=CODEX_MEMORY_PATH)
            collection = client.get_collection("project_codebase")
        except:
            return

        orgaos = Orgao.objects.all()
        if not orgaos:
            self.stdout.write(self.style.WARNING('⚠️ Nenhum órgão encontrado. Rode o popula_inicial primeiro.'))
            return

        for orgao in orgaos:
            self.stdout.write(f'   🩺 Diagnosticando: {orgao.nome}...')
            
            # Configurar Gemini (Hardcoded for stability)
            import google.generativeai as genai
            API_KEY = "AIzaSyBREWGg-uOUss7bZIoK0xqBU5svqvyCX6Y"
            genai.configure(api_key=API_KEY)

            # Gerar embedding da query
            query_text = f"Significado emocional e metafísico do {orgao.nome}"
            try:
                embedding_result = genai.embed_content(
                    model="models/embedding-001",
                    content=query_text,
                    task_type="retrieval_query"
                )
                query_vector = embedding_result['embedding']
            except:
                 query_vector = [0.0] * 768

            # Busca Deep Knowledge sobre o órgão
            results = collection.query(
                query_embeddings=[query_vector],
                n_results=1
            )
            
            if results['documents'][0]:
                wisdom = results['documents'][0][0]
                
                # Atualizando (Simulação de Enriquecimento)
                # No mundo real, faríamos um parse melhor. Aqui, vamos anexar ao campo representacao_emocional
                if len(orgao.representacao_emocional) < 50:
                    orgao.representacao_emocional = f"{wisdom[:200]}..."
                    orgao.save()
                    self.stdout.write(self.style.SUCCESS(f'      ✨ {orgao.nome} energizado com conhecimento.'))
            
        self.stdout.write(self.style.SUCCESS('🧘 SISTEMA HOLÍSTICO INTEGRADO.'))
