# crie uma função que identifique se um numero eh par ou impar

n =int(input("Digite um numero: "))

def par_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(par_impar(n))

