# crie um programa que pergunte ao cliente se é sua primeira compra
# depois pergunte o valor da compra
# se for a primeira compra do usuário e se for maior que R$500
# informe que ele ganhou um brinde e imprima uma mensagem de boas vindas 
# caso contrário imprima uma mensagem de agradecimento

# etapas
# 1) pergunte ao usuário se é a primeira compra dele
primeira_compra = input("É sua primeira compra conosco? (sim/não): ").strip().lower()
# print(primeira_compra)
# 2) pergunte ao usuário o total da compra
valor_compra = float(input("informe o valor total da sua compra: R$ "))
# 3) verifique a condição para o brinde
# 4) infporme se o usuário ganhou ou não o brinde
if primeira_compra == "sim" and valor_compra > 500:
    print("parabéns !! seja bem vinda(o) a MARTINS STORE , você ganhou um brinde pela sua primeira compra")
else:
    print("Obrigado pela compra!! volte sempre")
    