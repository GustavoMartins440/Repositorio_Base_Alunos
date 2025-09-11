# criar um jogo da forca onde o usuario tenta adivinhar um palavra secreta
# letra por letra, com até 6 erros peritidos. 

import random 

def jogar(): # funcao principal

    imprime_mensagem_abertura() # funcao para mensagem de abertura
    palavra_secreta = carrega_palavra_secreta() # escolhe uma palavra aleatoria de um arquiv.txt
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas) # mostra ao jogador os espacos da palavra, representador por "_"(_ _ _)

    # variaveis de controle
    enforcou = False # torna-se verdadeira se errar 6 vezes
    acertou = False # verdadeiro se acertar todas letras
    erros = 0 # conta o tanto de erros

    while (not enforcou and not acertou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra 
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu :(")
    print("Fim de jogo")

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute 

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta(nome_do_arquivo =r"C:\Users\Aluno_Programador\Desktop\pasta gmL\jogos\palavras_forca.txt"):
    arquivo = open (nome_do_arquivo, "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

#contextualizar o metodo "if (__name__ == "__main__")"significa que o arquivo esta
# sendo executado diretamente, nao apenas sendo lido para ser utilzado depois
if (__name__ == "__main__"):
    jogar()
