import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
        
def inserir(self, usuario, cpf, email, senha):
        try:
            sql = "Insert into cliente(codigo, usuario, email, senha) values('','{}','{}','{}','{}')".format(usuario, email, senha)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
def consultar(self, codigo):
        try:
            sql = "select * from cliente where codigo ='{}'".format(codigo)
            self.con.execute(sql)
            msg = ""
            
            for(codigo, usuario, cpf, email, senha) in self.con:
                msg = msg + "\nCódigo: {}, Usuário: {}, E-mail: {}, Senha: {}".format(codigo, usuario, email, senha)
            return msg
        except Exception as erro:
            return erro
        
def atualizar(self, cod, campo, novoDado):
        try:
            sql = "update cliente set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
def excluir(self, cod):
        try:
            sql = "delete from cliente where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(cod) 
        except Exception as erro:
            return erro
        
def tratarData(self, texto):
        separado = texto.split("/")
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)
    
def login(self, email, senha, emailInput, senhaInput)
    try:
        sql = 'select * from login'
        self.con.execute(sql)
        for (codigo, email, senha) in self.con:
            if email and senha == emailInput and senhaInput:
                return True
            else:
                print('/n')
            return False
    except Exception as erro:
        print (erro)
        
def loginValid1(self, email, senha, emailInput, senhaInput):
        try:
            if self.loginInsert1(email, senha, emailInput, senhaInput) == True:
                print('Logado com Sucesso !')
                print('\n')
            else:
                print('Login e Senha incorretos!')
                print('\n')
        except Exception as erro:
            print(erro)