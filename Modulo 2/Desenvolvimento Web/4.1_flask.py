from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome= request.form['nome']
        return f'Olá {nome}! seja bem vindo(a)'
    return render_template('ex_4-1.html')


if __name__ == '__main__':
    app.run(debug=True)
