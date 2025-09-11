# informações
nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# calcular IMC
imc = peso / (altura ** 2)

# exibir o IMC
print(f"\n, seu IMC é: {imc:.2f}")

# texto de avaliação do IMC
if imc >= 30.0:
    print("Cuidado com a Saúde!")
else:
    print("Tudo ok!")

# classificação de acordo com o calculo do IMC
if imc < 18.5:
 classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25.0:
 classificacao = "Peso normal"
elif 25.0 <= imc < 30.0:
 classificacao = "Sobrepeso"
elif 30.0 <= imc < 35.0:
 classificacao = "Obesidade Grau I"
elif 35.0 <= imc < 40.0:
 classificacao = "Obesidade Grau II"
else:
 classificacao = "Obesidade Grau III (mórbida)"

# exibição da classificação
print(f"Classificação: {classificacao}") 
