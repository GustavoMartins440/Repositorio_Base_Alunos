print("revisao for")
# for executa um bloco varias vezes 
frutas = ["maça","banana", "abacate", "caju", "melancia", "morango" ]
for fruta in frutas:
 print(f"eu gosto de {fruta}")
 carros = ["polo", "fit","peugeot", "bmw"]
 for carro in carros:
  print(f"vou comprar um {carro}") 
  # while executa um bloco 'enquanto' (while) uma condiçao for verdadeira
  contador = 1 
  while contador <= 5:
   print (f"contador: {contador}")
   contador = contador + 1 
 
 print("sai do while... ufa!!!")

 #crie um programa que peça e senha do cliente. a senha precisa ser "senha135
 # se a senha estiver correta imprima "senha ok" caso o contrario informe tb ][

#defina a senha correta 
senha_correta = "senha135" 
# solicita senha do cliente 
senha_cliente = input("digite a senha: ")
# verifica se a senha esta correta 
if senha_cliente == senha_correta:
     print ("senha ok")
else:
  print("senha incorreta")
  