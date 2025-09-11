#criar um codigo que consuma uma api de clima e informe a temperatura e a descriçãodo clima em um lugar especifico

#etapas
#1. Definir a chave de API e o link da requisição
#2. parametros da requisição
#3. fazer a requisição
#4. verificar se a requisição foi bem sucedida
#5. apresentar os resultados
import requests

api_key ='2a1ac38a32354cb7b19133643251408'
cidade = input('Digite o nome da cidade: ').strip()
url = f'http://api.weatherapi.com/v1/current.json'

parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt'
}

resposta = requests.get(url, params=parametros)
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['temp_c']
    descricao = dados ['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é: {temperatura}:°C ')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)
# http://api.weatherapi.com/v1/current.json
# 2a1ac38a32354cb7b19133643251408

