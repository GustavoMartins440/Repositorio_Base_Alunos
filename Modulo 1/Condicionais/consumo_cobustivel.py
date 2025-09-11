# switch case
# solicita os dados do usuario
distancia_percorrida = float(input("Digite a distância percorrida em km: "))
combustivel_gasto = float(input("Digite a quantidade de combustível gasto em litros: "))

# calcula o consumo medio
consumo_medio = distancia_percorrida / combustivel_gasto

# classifica o consumo usando o match-case
match consumo_medio: #abre O bloco de "casos".
    case valor if valor < 8:
        print("consumo menor que 8 km/l - DESEMPENHO RUIM")
    case valor if valor < 12:
        print("consumo entre 8 e 12 km/l - DESEMPENHO MEDIO")
    case _:
        print("Consumo maior ou igual a 12 km/l - ÓTIMO DESEMPENHO")
