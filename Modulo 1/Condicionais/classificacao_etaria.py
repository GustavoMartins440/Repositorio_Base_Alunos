# crie um programa de classificacao indicativa para eventos culturais

# L - livre para todos os pubicos 
# 10 - nao recomendado para menores de 10 anos
# 12 - nao recomendado para menores de 12 anos
# 14 - nao recomendado para menores de 14 anos
# 16 - nao recomendado para menores de 16 anos
# 18 - nao recomendado para menores de 18 anos
idade = int(input("Qual a sua idade? "))
if idade < 10:
    print("você apenas pode assitir conteúdos com classificação livre.")
elif idade >10 and idade <=12:
    print("Você pode assistir conteúdos com classificação para menores de 12 anos")
elif idade >12 and idade <=14:
    print("Você pode assistir conteúdos com classificação para menores de 14 anos")
elif idade >14 and idade <=16:
    print("Você pode assistir conteúdos com classificação para menores de 16 anos")
elif idade >16 and idade <=18:
    print("Você pode assistir conteúdos com classificação para menores de 18 anos")
else:
    print(" Você pode assistir a conteúdos com qualquer classificação etária.")