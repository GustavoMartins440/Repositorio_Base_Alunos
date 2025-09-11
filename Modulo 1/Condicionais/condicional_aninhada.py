print("Sistema de classificação por Idade")
print("==="*30)

# receba a idade do usuario
idade = int(input("Digite sua idade: "))
# virificacao inicial do usuario
if idade < 0: 
    print("ERRO: Idade inválida!")
else:
    # condicionais aninhadas para clasificar a idade 
    if idade < 12:
        print("Você é uma criança")
        # condicional aninhada para detalhes sobre crianças
        if idade <= 5: 
            print("primeira infância")
        else:
            print("Pré-Adolescente")
    elif idade < 18:
        print("Você é um adolescente.")
        if idade < 15:
            print("Adolescência inicial")
        else:
            print("Adolescência tardia.")
    elif idade < 60:
        print("Adulto")
        if idade < 30:
            print("Adulto jovem.")
        elif idade < 45:
            print("Adulto")
        else:
            print("adulto maduro.")
    else:
        print("Você é idoso.")
        if idade < 75: 
            print("terceira idade.")
        else:
            print("quarta idade.")
    print("==="*30)