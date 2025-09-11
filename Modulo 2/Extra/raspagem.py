import requests
import json
import pyautogui
import time
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Python"

response = requests.get(url)
response.encoding ='utf-8'

soup = BeautifulSoup(response.text,"html.parser" )

titulo = soup.title.string
primeiro_paragrafo = soup.find('p').text

# print(f'Título: {titulo}')
# print(f'Primeiro Paragrafo: {primeiro_paragrafo}')

dados = {
    "titulo":titulo,
    "primeiro_paragrafo":primeiro_paragrafo
}

dados_json = json.dumps(dados, indent=4, ensure_ascii=False)

with open('wikipedia_python.json', 'w', encoding='utf-8') as f:
    f.write(dados_json)

print("Abra o terminal e posicione o cursor,a digitação começa em 5 segundos ...")
time.sleep(5)
pyautogui.write(dados_json, interval=0.01)

