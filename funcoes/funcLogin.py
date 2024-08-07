import bcrypt
from modulos import *
from conexaoBD import *

#teste

def show_app(app_instance):
    app_instance.main_app.deiconify()  # Mostrar a janela principal do app
    app_instance.root.withdraw()  # Esconder a janela de login
    

def removeTuple(val):
    txt = val[0]
    print(val, txt)
    return txt

def getAcesso(self, user): #ATUALIZAR VARIÁVEL GLOBAL DE USER
    responsa(user)
    conexao = conectar_bd(self)
    cursor = conexao.cursor()
    query = "SELECT acesso FROM user WHERE nameUser = %s"
    cursor.execute(query, (user,))
    acesso = cursor.fetchone()
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
    pw = self.inputSenha.get()
    
    if(user and pw):
        try:
            conexao = conectar_bd(self)
            cursor = conexao.cursor()

            # verificarUser
            query = "SELECT nameUser, senha FROM user WHERE nameUser = %s"
            cursor.execute(query, (user,))
            result = cursor.fetchone()

            if result is None:
                messagebox.showwarning("Erro", "Usuário não encontrado!") 
                return

            nameUser, senha = result

            # Verifica a senha usando bcrypt
            if bcrypt.checkpw(pw.encode('utf-8'), senha.encode('utf-8')):
                show_app(self)
            else:
                messagebox.showwarning("Erro", "Senha incorreta!!!")
                
        finally:
            getAcesso(self, user)
            responsa(user)
            cursor.close()
            conexao.close()
    else:
        messagebox.showwarning("Erro", "Campos em branco! Por favor, preencha todos!")
