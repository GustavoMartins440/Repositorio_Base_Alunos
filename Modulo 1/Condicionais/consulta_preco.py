# crie um programa que consulte os precos dos produtos 
# e saia do programa quando solicitado pelo usuario

print("Códigos e produtos: ")
print("1 - arroz")
print("2 - café")
print("3 - refrigerante")
print("4 - suco")
print("5 - bolo de cenoura")
print("6 - barra de chocolate")
print("0 - SAIR")
while True:
    try: 
        # solicitar o codigo do produto ao usuario
        codigo = int(input("Digite o número do produto desejado: "))
        # usar o match-case para mostrar o preco com base no codigo
        match codigo:
            case 1:
                print("Produto: arroz - preço R$ 50,99")
            case 2:
                print("Produto: café - preço R$ 36,00")
            case 3:
                print("Produto: refrigerante - preço R$11,99")
            case 4:
                print("Produto: suco - preço R$11,99")       
            case 5:
                print("Produto: bolo de cenoura - preço R$24,99")
            case 6:
                print("Produto: barra de cholate - preço R$9,99")
            case 0:
                print("saindo do programa")
                break # sai do looping e encerra o programa
            case _:
                print("Código inválido. Por favor, tente novamente.")
    except ValueError:
        print("entrada inválida. Digite um número inteiro.")
