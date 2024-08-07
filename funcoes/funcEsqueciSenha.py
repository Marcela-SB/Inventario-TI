from modulos import *
from conexaoBD import *

def esqueciSenha(self):
    email = self.inputEmailEsqSen.get()
    pw = self.inputSenhaEsqSen.get()

    if email and pw:
        try:
            conexao = conectar_bd(self)
            cursor = conexao.cursor()

            # verificarUser
            cursor.execute("SELECT email FROM user WHERE email = %s", (email,))
            usuario = cursor.fetchone()

            if usuario is None:
                messagebox.showwarning("Erro", "Usuário não encontrado!") 
                return

            pwHashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()) # hashing da senha (encriptando)

            cursor.execute("""
                UPDATE user
                SET senha = %s
                WHERE email = %s;
            """, (pwHashed, email,)) 
            conexao.commit()

            messagebox.showinfo("Sucesso", "Senha atualizada com sucesso!")
            self.janelaEsqueciSenha.destroy()  # Fecha a janela        
                
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showwarning("Atenção", "Campos em branco! Por favor, preencha todos!")