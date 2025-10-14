#crie um app flask basico que exibe "Olá, Mundo!" na rota principal (/)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Mundo!'


if __name__ == '__main__':
    app.run(debug=True)

