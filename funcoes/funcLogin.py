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

def validarUser(self):
    user = self.inputLogin.get()

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


def novoUser(self):
    messagebox.showinfo("Info", "Botão Novo User")
