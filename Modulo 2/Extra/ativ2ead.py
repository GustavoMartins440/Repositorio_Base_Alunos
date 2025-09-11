import requests
from bs4 import BeautifulSoup

def coletar_manchetes(url):
    response = requests.get(url)
    response.raise_for_status()  # garante que a requisição deu certo

    soup = BeautifulSoup(response.text, 'html.parser')

    # Exemplo para G1 (globo.com) - as manchetes principais ficam em h3 com classe 'feed-post-link'
    manchetes = soup.find_all('a', class_='feed-post-link')

    print(f"Manchetes do site {url}:\n")
    for i, manchete in enumerate(manchetes[:10], 1):  # limita a 10 manchetes
        print(f"{i}. {manchete.get_text(strip=True)}")

if __name__ == '__main__':
    url = 'https://g1.globo.com/'  # URL do site que quer coletar as manchetes
    coletar_manchetes(url)
