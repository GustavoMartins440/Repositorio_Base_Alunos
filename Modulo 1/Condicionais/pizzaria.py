# exibe o menu de pizzas 
print("Crdápio da pizzaria Gustavo")
print("1 - Marguerita")
print("2 - Calabresa")
print("3 - Frango com catupiry")
print("4 - Mussarela")
print("5 - Quatro Queijos")
print("6 - SAIR")
while True:
    try:
        #solicitacao do codigo da piiza
        codigo_pizza = int(input("Digite o numero da pizza desejada: "))
        # usar metch-case para mostrar os sabores e precos
        match codigo_pizza:
            case 1:
                print("Pizza Marguerita - R$45,00")
            case 2:
                print("Pizza Calabresa - R$40,00")
            case 3:
                print("Pizza Frango com catupiry - R$45,00")
            case 4:
                print("Pizza Mussarela - R$35,00")
            case 5:
                print("Pizza Quatro Queijos - R$55,00")
            case 6:
                print("SAIR")
                break # sai do looping e encerra o programa
            case _:
                print("Código inválido. Por favor, tente novamente.")
    except ValueError:
        print("entrada inválida. Digite um número inteiro.")
            