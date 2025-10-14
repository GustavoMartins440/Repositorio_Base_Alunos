from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de progamadores.'

@app.route('/lista')
def lista():
    alunos = ['Gustavo', 'Diego', 'Gabriel', 'Bernardo']
    return render_template('ex_3-2.html',lista=alunos)



if __name__ == '__main__':
    app.run(debug=True)
