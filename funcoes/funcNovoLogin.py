import bcrypt
from modulos import *
from conexaoBD import *

def validarAcesso(self, user, pw):
    try:
        conexao = conectar_bd(self)
        cursor = conexao.cursor()

        cursor.execute("SELECT nameuser, acesso, senha FROM user WHERE nameuser = %s", (user,))
        usuario = cursor.fetchone()

        if usuario is None:
            messagebox.showerror("Erro", "Login ou senha incorreto(s)!")
            return

        nameuser, acesso, senhaHashed = usuario

        # Verifica a senha usando bcrypt
        if nameuser==user and bcrypt.checkpw(pw.encode('utf-8'), senhaHashed.encode('utf-8')):  # se usuário e senha estiverem corretos
            if acesso == "admin":
                from novoUser import criarNovoUser  # Importar aqui para evitar o ciclo
                criarNovoUser(self)
            else:
                messagebox.showwarning("Acesso negado", "Você não possui acesso para essa função.")
        else:
            messagebox.showerror("Erro", "Login ou senha incorreto(s)!")

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")      
    finally:
        cursor.close()
        conexao.close()

def adicionarNovoUser(self):
    login = self.inputNovoLogin.get()
    email = self.inputNovoEmail.get()
    acesso = self.selAcesso.get()
    pw1 = self.inputSenha1.get()
    pw2 = self.inputConfirmSenha.get()

    if login and email and acesso and pw1 and pw2:
        if pw1 == pw2:
            try:
                conexao = conectar_bd(self)
                cursor = conexao.cursor()

                pwHashed = bcrypt.hashpw(pw1.encode('utf-8'), bcrypt.gensalt()) # hashing da senha (encriptando)

                cursor.execute("INSERT INTO user (nameuser, email, acesso, senha) VALUES (%s, %s, %s, %s)", (login, email, acesso, pwHashed))
                conexao.commit()

                messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
                self.janela.destroy()  # Fecha a janela de criação de usuário

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")    
            finally:
                cursor.close()
                conexao.close()
        else:
            messagebox.showwarning("Erro", "Senhas informadas são diferentes, por favor conferir.")
    else:
        messagebox.showwarning("Erro", "Campos em branco! Por favor, preencha todos!")
