from flask import Flask

app = Flask(__name__)


@app.route('/hello/')
@app.route("/hello/<nome>")
def hello(nome=""):
    return "<h1>Bom Dia {} </h1>".format(nome)


@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID =-1):
    if postID >= 0:
        return "Blog info {} ".format(postID)
    else:
        return "Todo conteúdo do Blog "


@app.route('/blog/<float:postID>')
def blog2(postID =-1):
    if postID >= 0:
        return "Blog float {} ".format(postID)
    else:
        return "Todo conteúdo do Float "

if __name__ == '__main__':
    app.run(debug=True)
