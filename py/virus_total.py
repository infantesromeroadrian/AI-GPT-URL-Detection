# virus_total_analysis.py
import requests
from api_keys_loader import load_virustotal_api_key

def analyze_url_with_virustotal(url):
    api_key = load_virustotal_api_key()
    headers = {"x-apikey": api_key}
    params = {"url": url}
    response = requests.post('https://www.virustotal.com/api/v3/urls', headers=headers, data=params)
    analysis_id = response.json()['data']['id']
    analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    analysis_response = requests.get(analysis_url, headers=headers)
    return analysis_response.json()
