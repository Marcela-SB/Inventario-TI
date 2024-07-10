from modulos import *

'''def obterSenha():
    senha = None
    popup = tk.Toplevel()
    popup.title("Login")
    popup.configure(bg= "#29273A")
    popup.geometry("500x200") # Largura x Altura
    popup.resizable(False, False)          #RESPONSIVIDADE
    popup.focus_force()
    popup.grab_set()
    
    tk.Label(popup, text="Digite a senha:").pack(pady=10)
    
    entrada = tk.Entry(popup, show="*")
    entrada.pack(pady=15)
    
    def enviarSenha():
        nonlocal senha
        senha = entrada.get()
        popup.destroy()
    
    tk.Button(popup, text="Entrar", command=enviarSenha).pack(pady=10)
    
    # Espera o popup ser fechado
    popup.wait_window(popup)
    
    return senha'''


# ----------- CONEXÃO COM O BANCO DE DADOS -----------
def conectar_bd(self):
    senha = "cfeb6252a2;" #obterSenha()
    '''if senha is None:
        messagebox.showerror("Erro", "Nenhuma senha fornecida.")
        return None'''
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="admin",
            password= "admin1234",
            database="inventario"
        )
        #messagebox.showinfo("Conexão", "Conexão com o banco de dados estabelecida com sucesso!")
        return conexao
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
        return None