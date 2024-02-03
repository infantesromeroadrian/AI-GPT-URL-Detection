# streamlit_app.py
import streamlit as st
from virus_total import analyze_url_with_virustotal
from openai_gpt import get_gpt_opinion_on_url

st.title('Analizador de URLs')

url = st.text_input('Ingresa la URL para analizar:')
if url:
    st.write('Analizando URL con VirusTotal...')
    analysis_result = analyze_url_with_virustotal(url)
    st.json(analysis_result)  # Muestra el resultado JSON directamente como un ejemplo

    st.write('Obteniendo opinión de GPT sobre la URL...')
    gpt_opinion = get_gpt_opinion_on_url(analysis_result)
    st.write(gpt_opinion)
