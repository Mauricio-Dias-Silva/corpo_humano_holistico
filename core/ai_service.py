# core/ai_service.py
import google.generativeai as genai
from django.conf import settings
from datetime import datetime
import pytz

# core/ai_service.py
# ... (imports no topo) ...

def get_aura_greeting(user, perfil):
    try:
        # ... (configuração do genai e lógica da hora do dia, como antes) ...
        fuso_horario_br = pytz.timezone('America/Sao_Paulo')
        hora_atual = datetime.now(fuso_horario_br).hour
        periodo_dia = "Manhã" # ...

        # Acessando o campo do nosso model PerfilUsuario
        nivel_atividade_texto = perfil.get_nivel_atividade_display() if perfil else "não informado"

        prompt = f"""
        Você é Aura, uma IA assistente de bem-estar.
        O usuário '{user.username}' está na página inicial.
        O período do dia é: {periodo_dia}.
        O nível de atividade dele é: '{nivel_atividade_texto}'.
        Sua tarefa é criar uma saudação curta e calorosa, com uma dica de bem-estar sutilmente adaptada ao nível de atividade e período do dia.
        """

        # ... (resto do código que gera o conteúdo) ...
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro na API da IA: {e}")
        return f"Olá, {user.username}! Seja bem-vindo(a). (Erro ao conectar com a IA)"