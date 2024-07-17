from modulos import *
from conexaoBD import *



def show_app(app_instance):
    app_instance.main_app.deiconify()  # Mostrar a janela principal do app
    app_instance.root.withdraw()  # Esconder a janela de login

def verificarSenha(self, pw):
    
    conexao = conectar_bd(self)
    cursor = conexao.cursor()
    query = "SELECT senha FROM user WHERE senha = %s"
    cursor.execute(query, (pw,))
    result = cursor.fetchall()
    sExiste = False
    for c in result:
        if(c == (pw,)):
            sExiste = True
            show_app(self)
    if(sExiste == False):
        messagebox.showwarning("Erro", "Senha incorreta!!!")

def removeTuple(val):
    txt = val[0]
    print(val, txt)
    return txt

def getAcesso(self, user):
    responsa(user)
    conexao = conectar_bd(self)
    cursor = conexao.cursor()
    query = "SELECT acesso FROM user WHERE nameUser = %s"
    cursor.execute(query, (user,))
    acesso = cursor.fetchall()
    acesso = removeTuple(acesso[0])
    NivelUser(acesso)
    print(acesso)
    '''AcExiste = False
    for c in acesso:
        if(c == (self.user,)):
            AcExiste = True
            show_app(self)
    if(AcExiste == False):
        messagebox.showwarning("Erro", "acesso negado? incorreta!!!")'''


def validarUser(self):
    global nameUser
    user = self.inputLogin.get()
    getAcesso(self, user)
    pw = self.inputSenha.get()
    
    if(user and pw):
        try:
            conexao = conectar_bd(self)
            cursor = conexao.cursor()

            # verificarUser
            query = "SELECT nameUser FROM user WHERE nameUser = %s"
            cursor.execute(query, (user,))
            result = cursor.fetchall()
            existe = False
            for c in result:
                if(c == (user,)):
                    existe = True
                    verificarSenha(self, pw)
            if (existe == False):
                messagebox.showwarning("Erro", "Usuário não encontrado!") 
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showwarning("Erro", "Campos em branco! Por favor, preencha todos!")
'''def chamarConexao(self):
        iniciar = None
        while(iniciar == None):
            iniciar = conectar_bd(self)'''

