# crie um sistema de login simples em python , onde o usuario precisara
# inserir um nome de um usuario para acessar o sistema

# dados de login 
usuario_cadastrado = "usuario123"
senha_cadastrada = "senha456"

# solicitar nome de usuario e senha
nome_usuario = input("Digite seu nome de usuário: ").strip().lower()
senha = input("Digite sua senha: ").strip().lower()

# verificação do login
if nome_usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Login bem sucedido! Bem vindo(a)", nome_usuario)
else:
    print("Nome de usuario ou senha incorretos, tente novamente. ")

