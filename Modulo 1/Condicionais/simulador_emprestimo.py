# crie um programa que simule um sistema de emprestimo para um banco.
# o prgrama solicita ao usuario o valor desejado para emprestimo e a quantidade de pacelas desejadas
# com base nas informações fornecidas , o programa cabula o valor das parcelas e verifique 
# pode ser aprovado, considerando as seguintes regras:
# o valor minimo para emprestimo é R$  1000,00
# o valor maximo para emprestimo é R# 50.000,00
# a quantidad minima de parcelas é 6 e a maxima 36
# o valor da parcela não pode ultrapassar 30% da renda mensal do cliente

print("SImulador de Empréstimo\n")
# criacao das variaveis
valor_emprestimo = float (input("Digite o valor desejado para o empréstimo: R$ "))
num_parcelas = int (input("Digite a quantidade de parcelas desejadas (6 a 36): "))
renda_mensal = float (input("Digite sua renda mensal: R$ "))

valor_parcela = valor_emprestimo / num_parcelas
renda_permitida = renda_mensal * 0.3
if valor_emprestimo < 1000 or valor_emprestimo >50000: 
    resultado = "Empréstimo não aprovado: valor fora dos limites permitidos."

elif num_parcelas < 6 or num_parcelas > 36:
    resultado = "Empréstimo não aprovado: quantidade de parcelas inválida"
elif valor_parcela > renda_permitida:
    resultado = f"Empréstimo não aprovado: valor das parcelas excede 30% da renda mensal"

else:
    resultado = f"Empréstimo aprovado. valor das parcelas: R$ {valor_parcela:.2f}"
print("\nResultado:")
print(resultado)
