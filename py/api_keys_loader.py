# config.py

# Carga la clave API de OpenAI
def load_openai_api_key():
    with open('/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Udemy/AIGenerative/URLFakeDetector/data/Secret_OPENAI_Key.txt', 'r') as file:
        return file.readline().strip()

# Carga la clave API de VirusTotal
def load_virustotal_api_key():
    with open('/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Udemy/AIGenerative/URLFakeDetector/data/Secret_VirusTotal_key.txt', 'r') as file:
        return file.readline().strip()
