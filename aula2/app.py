from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"

def teste():
    return "<h1>Estudando Flask</h1>"

def estudo():
    return "<h2>Criando Rota</h2>"

app.add_url_rule("/teste", "teste",teste)
app.add_url_rule("/estudo","estudo", estudo)

    

if __name__ == '__main__':
    app.run(debug=True, port="3000")
