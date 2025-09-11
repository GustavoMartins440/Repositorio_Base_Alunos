import json
pessoa ={"nome":"Gustavo","Idade":17,"Estudante":False}
json_strings = json.dumps(pessoa)
print(json_strings)
