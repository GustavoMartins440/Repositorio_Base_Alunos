import requests
import json
import pyautogui
import time
from bs4 import BeautifulSoup

# URL do resumo da partida mais recente (volta da final do Paulista 2025)
url = "https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_2025"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")


texto = ""
paras = soup.find_all('p')
for p in paras:
    if "16 de março" in p.text or "27 de março" in p.text or "Corinthians empata com o Palmeiras e conquista o título" in p.text:
        texto += p.text + "\n\n"

dados = {
    "resumo_final_16_mar": None,
    "resumo_final_27_mar": None,
    "detalhes": texto.strip()
}

parts = texto.split("\n\n")
for part in parts:
    if "16 de março" in part:
        dados["resumo_final_16_mar"] = part
    elif "27 de março" in part or "empatou sem gols" in part:
        dados["resumo_final_27_mar"] = part

dados_json = json.dumps(dados, indent=4, ensure_ascii=False)

with open('derby_paulista_resumo.json', 'w', encoding='utf-8') as f:
    f.write(dados_json)

print("Abra o terminal e posicione o cursor, a digitação começa em 5 segundos ...")
time.sleep(5)
pyautogui.write(dados_json, interval=0.01)
