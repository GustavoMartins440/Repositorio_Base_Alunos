# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se o segundo número é diferente de zero antes de dividir
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Indefinida (divisão por zero)"

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
