from openai_gpt import OpenAIGPT
from virus_total import VirusTotal


def main():
    # Instancia de la clase para interactuar con GPT de OpenAI
    gpt = OpenAIGPT('/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Udemy/AIGenerative/URLFakeDetector/data/Secret_OPENAI_Key.txt')

    # Instancia de la clase para interactuar con VirusTotal
    virus_total = VirusTotal(
        '/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Udemy/AIGenerative/URLFakeDetector/data/Secret_VirusTotal_key.txt')

    # Ejemplo de cómo usar el GPT para obtener una respuesta
    prompt = "¿Cuál es el mejor lenguaje de programación?"
    respuesta_gpt = gpt.obtener_completion(prompt)
    print("Respuesta GPT:", respuesta_gpt)

    # Ejemplo de cómo usar VirusTotal para verificar una URL
    url = "http://ejemplo-de-url-a-analizar.com"
    resultado_virus_total = virus_total.check_url(url)
    print("Resultado VirusTotal:", resultado_virus_total)


if __name__ == "__main__":
    main()
