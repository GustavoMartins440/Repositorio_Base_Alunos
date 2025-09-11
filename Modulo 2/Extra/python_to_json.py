import json

json_data = '{"nome":"ana","idade":30,"estudante":true}'

dados_python = json.loads(json_data)

print(dados_python['nome'])
print(dados_python['idade'])
print(dados_python['estudante'])
