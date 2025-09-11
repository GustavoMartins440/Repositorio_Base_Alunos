# crie um programa que solicite a nota de um aluno e informe o conceito recebido.
# conceitos => A = excelente(nota igual ou maior que 9), B = muito bom(nota igual ou maior que 8)
# C = bom(nota igual ou maior que 7), D = regular (nota igual ou maior que 6)
# E = insuficiente(nota igual ou menor que 6)
nota = float(input("Qual a sua nota? "))
if nota >9:
    print("Excelente")
elif nota >= 8:
    print("Muito bom")
elif nota >= 7:
    print("Bom")
elif nota >= 6:
    print("Regular")
elif nota <= 6:
    print("Insuficiente")

    