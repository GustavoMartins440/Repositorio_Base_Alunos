#função para identificar se um numero eh par ou impar

numero =int(input("digite um numero: "))

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(par_impar(numero))
