# Exercício 2.2: Links entre rotas
# Adicione um menu de navegação simples com links
# para todas as suas rotas(/,/sobre,/saudacao, etc.).
# Passar a varivél através do url for dentro do script
# html: ("{{url_for('saudacao', nome='Jõao' ) }}")
# 'saudacao' é o nome da funcao Python que define a rota.
# nome='João' está passando o valor para a variável que a rota espera (<nome>)

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de progamadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá, {nome}! seja bem-vindo(a)!!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    dobro  = numero*2
    return f'O dobro de {numero} é {dobro}.'





if __name__ == '__main__':
    app.run(debug=True)
