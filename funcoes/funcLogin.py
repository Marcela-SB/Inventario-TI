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
    
    user = self.inputNovoLogin.get()
    eml = self.inputNovoEmail.get()
    acss = self.selAcesso.get()
    pw = self.inputSenha1.get()
    cpw = self.inputConfirmSenha.get()

    if(pw == cpw):
    
        try:
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()

            cursor.execute("")
            cursor.execute("INSERT INTO users (login, email, acesso, senha) VALUES (%s, %s, %s, %s)", ())
            conexao.commit()
            messagebox.showinfo("Sucesso", "Movimentação criada com sucesso!")
            
            self.janelinha.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar nova movimentação: {err}")
        finally:
            cursor.close()
            conexao.close()

    else:
        messagebox.showerror("Senhas", "Senha e senha de confirmação estão diferentes, por favor verificar!")

