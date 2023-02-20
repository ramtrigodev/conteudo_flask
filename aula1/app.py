from flask import Flask # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Rota do Index
def index():
  return 'Index'

@app.route('/teste') # Rota para outra página teste
def teste():
  return 'Teste'

if __name__ == '__main__':
  app.run(debug=True)