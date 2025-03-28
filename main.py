# ARQUIVOS DA MODULARIZAÇÃO
from modulos import *
from conexaoBD import*
from novoUser import *
from mudarSenha import *
from funcoes.funcLogin import *
from funcoes.funcNovoLogin import *
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
        self.root.geometry("400x210")  # Largura x Altura
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


# BOTÕES
        # LABEL para mudança de senhas
        self.btEsqueciSenha = Label(
            self.root, 
            bg="#D9D9D9",
            fg="blue",
            text="Esqueci a senha", 
            font=("Inter Regular", 12 * -1),
            relief="flat", 
            borderwidth=2,
            padx=10,
            pady=5,
            cursor="hand2"
        )
        self.btEsqueciSenha.place(
            relx = 0.56,
            rely = 0.54,
            height= 35,
            width= 160
        )
        self.btEsqueciSenha.bind("<Button-1>", mudarSenha)

        # Botão de Login para demonstrar o fluxo
        self.btLogin = Button(
            self.root, 
            bg="#29273A",
            fg= "#FFFFFF",
            text="Login", 
            font=("Inter Regular", 20 * -1),
            relief="flat", 
            border=2,
            command=lambda: validarUser(self) #show_app(self)
        )
        self.btLogin.place(
            relx = 0.68,
            rely = 0.72,
            height= 35,
            width= 80
        )
        # função para acionar botão "LOGIN" ao apertar "ENTER"
        self.root.bind('<Return>', lambda event:  show_app(self)) #validarUser(self)) 
        

        # Botão para adicionar novos Users
        self.btNovoUser = Button(
            self.root,
            fg= "#29273A",
            text="Novo User", 
            font=("Inter Regular", 20 * -1),
            relief="flat", 
            border=2,
            command=lambda: validarAcesso(self, self.inputLogin.get(), self.inputSenha.get())
        )
        self.btNovoUser.place(
            relx = 0.2,
            rely = 0.72,
            height= 35,
            width= 100
        )
        

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
            rely = 0.12
        )
        self.inputLogin = Entry(self.root, font=50)
        self.inputLogin.place(
            relx = 0.3,
            rely = 0.12,
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
            rely = 0.42
        )
        self.inputSenha = Entry(
            self.root, 
            font=50, 
            show="*"
        )
        self.inputSenha.place(
            relx = 0.3,
            rely = 0.42,
            relwidth=0.58, 
            height=30
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