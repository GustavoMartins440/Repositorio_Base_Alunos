# Função para calcular a média e determinar a situação acadêmica
def situacao_academica(nota1, nota2, nota3):
    # Calcula a média aritmética
    media = (nota1 + nota2 + nota3) / 3
    # Exibe a média calculada
    print(f"Média: {media:.2f}")
    # Determina a situação acadêmica com base na média
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Em recuperação"
    else:
        return "Reprovado"
# Leitura das notas do aluno
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
     # Chama a função e exibe a situação acadêmica
    resultado = situacao_academica(nota1, nota2, nota3)
    print(f"Situação acadêmica: {resultado}")
except ValueError:
    print("Por favor, insira valores numéricos válidos para as notas.")