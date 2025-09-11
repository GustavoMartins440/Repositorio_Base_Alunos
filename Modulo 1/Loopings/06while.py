bombons = 4  # variavel qu inicia a contagem 

while bombons > 0: # enquanto bombons  0 o while continua executando
    print(f"Eu tenho {bombons} bombons.") # informa o numero de bombons atual
    bombons -= 1 # diminui um bombom
    print(f"Comi 1 e fiquei com {bombons} bombons") # informa a quantidade de bombons após a subtração 
    if bombons == 0: # quando a quantidade  de bombons for zero
        print("Acabaram os bombons.") # informa que acabou 

