from flask import Flask, render_template, request
from model import model
import this

this.usuario = ""
this.email = ""
this.senha = ""
this.dados = ""
this.modelo = model()
this.codigo = 0
this.msg = ""
this.campo = ""
this.dado = ""

pessoa = Flask(__name__)

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.usuario     = request.form['tNewUsuario']
        this.email       = request.form['tNewEmail']
        this.senha       = request.form['tNewSenha']
        this.dados       = this.modelo.inserir(this.usuario, this.email, this.senha)
    return render_template('Cadastro.html', titulo="Página Principal", resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET','POST'])
def consultarTudo():
    if request.method == 'POST':
        this.codigo   = request.form['tNewCodigo']
        this.msg      = this.modelo.consultar(this.codigo)
    return render_template('consultar.html', titulo="Consultar", dados=this.msg)

@pessoa.route('/atualizar.html', methods=['GET','POST'])
def atualizarDado():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizar(this.codigo, this.campo, this.dado)
    return render_template('atualizar.html', titulo="Atualizar", dados=this.msg)

@pessoa.route('/excluir.html', methods=['GET','POST'])
def excluirDado():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg    = this.modelo.excluir(this.codigo)
    return render_template('excluir.html', titulo="Excluir", dados=this.msg)

@pessoa.route('/', methods=['GET', 'POST'])
def loginCliente():
    if request.method == 'POST'
        this.email  = request.form['tNewEmail']
        this.senha = request.form['tNewSenha']
        this.msg = this.modelo.consultar(this.email, this.senha)
    return render_template('Login.html', titulo="Consultar", dados=this.msg)

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)
