# crie um programa que verifique infrações de trânsito: rodízio e velocidade

# etapas
# 1) PERGUNTE SE HOJE É RODÍZIO DO CARRO
rodizio = input("Hoje é rodizio do seu veículo? (sim/não)").strip().lower()
# 2) pergunte a velocidade do carro
velocidade = float(input("qual a velocidade atual do veículo (Km/h)? "))
# 3) defina o limite de veloidade da via
limite = 60
# 4) verifique as infrações
if rodizio == "sim" and velocidade > limite:
    print("Você está dirigindo no dia do seu rodizio e acima da velocidade permitida.\n")
    print("você será autuado por ambas infrações.") 
elif rodizio == "sim":
    print("Você está dirigindo no dia do seu rodizio e sera autuado por isso")
elif velocidade > limite:
    print("Você esta dirigindo acima do limite de velocidade permitida " \
          "e será autuado por excesso de velocidade")
else:
    print("tudo certo! você esta dentro da lei. dirija com segurança!.")