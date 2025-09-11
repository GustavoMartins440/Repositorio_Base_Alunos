
# criamos uma lista com as informações dos alunos
alunos = [
    {"nome": "joão", "idade":20, "nota": 7.5},
    {"nome": "laura", "idade":43, "nota": 9.5},
    {"nome": "gustavo", "idade":30, "nota": 7.0},
    {"nome": "maria", "idade":26, "nota": 8.5}
    ]
# criamos duas variaveis
total_notas = 0 # essa variavel sera nosso contador para somar as notas dos alunos
quantidade_alunos = len(alunos) # essa variavel vai informar a quantidade de alunos atraves da funcao len

for aluno in alunos: # esse for ira percorrer cada objeto(aluno)
    total_notas += aluno["nota"]
media_notas = total_notas/ quantidade_alunos
print(f"A média das notas dos alunos é {media_notas:.2f}")
