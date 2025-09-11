# Função para converter de Dólar para Real
def dolar_para_real(valor_em_dolar, taxa_cambio):
    return valor_em_dolar * taxa_cambio  # Multiplica o valor em dólar pela taxa de câmbio

# Função para converter de Real para Dólar
def real_para_dolar(valor_em_real, taxa_cambio):
    return valor_em_real / taxa_cambio  # Divide o valor em real pela taxa de câmbio

# Define a taxa de câmbio (exemplo: 1 dólar = 5.15 reais)
taxa_cambio = 5.15

# Exibe as opções para o usuário
print("Conversor de Moeda")
print("1. Dólar para Real")
print("2. Real para Dólar")

# Solicita ao usuário que escolha a opção de conversão
opcao = input("Escolha uma opção (1 ou 2): ")

# Se o usuário escolher a opção 1, converte de dólar para real
if opcao == "1":
    valor = float(input("Digite o valor em dólares: $"))  # Solicita o valor em dólares
    convertido = dolar_para_real(valor, taxa_cambio)      # Chama a função de conversão
    print(f"R${convertido:.2f}")                          # Exibe o resultado formatado com duas casas decimais

# Se o usuário escolher a opção 2, converte de real para dólar
elif opcao == "2":
    valor = float(input("Digite o valor em reais: R$"))   # Solicita o valor em reais
    convertido = real_para_dolar(valor, taxa_cambio)      # Chama a função de conversão
    print(f"${convertido:.2f}")                           # Exibe o resultado formatado com duas casas decimais

# Se a opção for inválida, exibe uma mensagem de erro
else:
    print("Opção inválida!")