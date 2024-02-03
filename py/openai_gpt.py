# openai_gpt.py


import openai
from api_keys_loader import load_openai_api_key

def get_gpt_opinion_on_url(url_analysis):
    openai.api_key = load_openai_api_key()
    prompt = f"Analiza esta URL desde una perspectiva de ciberseguridad: {url_analysis}. ¿Es segura o maliciosa?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente experto en ciberseguridad especializado en análisis de URLs."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].message['content']
