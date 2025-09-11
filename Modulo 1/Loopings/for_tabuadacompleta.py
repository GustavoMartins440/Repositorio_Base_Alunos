print("tabuada de todos os numeros 1 a 10 usando for")
print("_"*50)
for numero in range(1,11):
    print(f"\n tabuada do {numero}: ")
    print("-"*20)

    for i in range (1,11):
        resultado = numero*i
        print(f"{numero} X {i} = {resultado}")
