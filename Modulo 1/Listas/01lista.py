numeros = [1,2,3,4,5,6,7] # sintaxe para construir uma lista => nome = []

print(type(numeros)) # a funcao "type" informa o tipo da variavel

print(numeros[1]) # funcao para buscar um elemento especifico da lista

print(numeros[-1]) # para conhecermos o ultimo elemento de uma lista

numeros[2] = 10 # substitui um elemento que estava no indice 2
print(numeros)

numeros.append(8) # adicionando um elemento no FINAL  de uma lista
print(numeros) 

numeros.remove(4) # remove o objeto especifico de uma lista
print(numeros) 

