#Instalando Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html')


@app.route("/QuemSomos/")
def QuemSomos():

    return render_template('QuemSomos.html')

@app.route("/Contatos/")
def Contato():

    return render_template('Contatos.html')

if __name__ == '__main__':
    app.run(debug=True)
