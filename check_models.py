
import google.generativeai as genai

API_KEY = "AIzaSyBREWGg-uOUss7bZIoK0xqBU5svqvyCX6Y"
genai.configure(api_key=API_KEY)

print("Listando modelos disponíveis...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name} ({m.display_name})")
except Exception as e:
    print(f"Erro ao listar modelos: {e}")
