nome = input("Qual é o seu nome?? :")
idade = int(input("Quantos anos você tem? :"))
possui_carteira = input("Possui CNH? \n (1-sim/ 2-não)")

if idade >= 18:
    if possui_carteira == "1":
        print("Está liberado para dirigir!!")
    else:
        print("Não pode dirigir! ")
else:
    print("Menor de idade, não esta liberado para dirigir")
    