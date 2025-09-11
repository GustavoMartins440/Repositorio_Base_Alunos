idade = float(input("Digite a sua idade: "))
if idade < 16:
    print("Não pode votar.")
elif (idade >= 16 and idade < 18) or idade > 70:
    print("Pode votar mas é facultativo.")
else:
    print("Voto obrigatório.")

    