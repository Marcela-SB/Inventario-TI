# ARQUIVOS DA MODULARIZAÇÃO
from modulos import *
from conexaoBD import*
from funcoes.funcLogin import *
from app import *


class Application:
    def __init__(self, root):
        self.root = root
        self.login_window()
        self.app_window()  # Cria a janela principal, mas mantém oculta

# ----------- LOGIN -----------
    def login_window(self):
        self.root.title("Login Sistema de Inventário")
        self.root.configure(bg="#D9D9D9")
        self.root.geometry("400x200")  # Largura x Altura
        self.root.resizable(False, False)  # RESPONSIVIDADE

# FRAME PRINCIPAL
        '''self.logFrame = Frame(
            self.root, 
            bd=4, 
            bg="#D9D9D9",
            highlightbackground="#9B9B9B",
            highlightthickness= 1.5
        )
        self.logFrame.place(         # POSIÇÃO (relativa) DO FRAME PRINCIPAL
            relx= 0.01, 
            rely=0.205, 
            relwidth=0.98, 
            relheight=0.78
        )'''

# LABELS
        self.lbLogin = Label( 
            self.root, 
            text="Login:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbLogin.place(
            relx = 0.1,
            rely = 0.15
        )
        self.inputLogin = Entry(self.root, font=50)
        self.inputLogin.place(
            relx = 0.3,
            rely = 0.15,
            relwidth=0.58, 
            height=30
        )

        self.lbSenha = Label( 
            self.root, 
            text="Senha:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbSenha.place(
            relx = 0.1,
            rely = 0.45
        )
        self.inputSenha = Entry(
            self.root, 
            font=50, 
            show="*"
        )
        self.inputSenha.place(
            relx = 0.3,
            rely = 0.45,
            relwidth=0.58, 
            height=30
        )

# BOTÕES
        # Botão de Login para demonstrar o fluxo
        self.btLogin = Button(
            self.root, 
            bg="#29273A",
            fg= "#FFFFFF",
            text="Login", 
            font=("Inter Regular", 20 * -1),
            relief="flat", 
            border=2,
            command=lambda: validarUser(self)
        )
        self.btLogin.place(
            relx = 0.68,
            rely = 0.7,
            height= 35,
            width= 80
        )

        # Botão para adicionar novos Users
        self.btNovoUser = Button(
            self.root,
            fg= "#29273A",
            text="Novo User", 
            font=("Inter Regular", 20 * -1),
            relief="flat", 
            border=2,
            command=lambda: novoUser(self)
        )
        self.btNovoUser.place(
            relx = 0.2,
            rely = 0.7,
            height= 35,
            width= 100
        )


# ----------- APP -----------
    def app_window(self):
        self.main_app = App(self.root)
        self.main_app.withdraw()  # Esconde a janela principal até que o login seja feito
        

    
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()


# ----------- FRAME PRINCIPAL -----------
    '''def frameDaTela(self):
        self.frame_principal = Frame(       # DETALHES DO FRAME PRINCIPAL
            self, 
            bd=4, 
            bg="#D9D9D9",
            highlightbackground="#9B9B9B",
            highlightthickness= 1.5
        )
        self.frame_principal.place(         # POSIÇÃO (relativa) DO FRAME PRINCIPAL
            relx= 0.01, 
            rely=0.205, 
            relwidth=0.98, 
            relheight=0.78
        )'''