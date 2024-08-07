from modulos import *
from funcoes.funcNovoLogin import adicionarNovoUser

def criarNovoUser(self):
    self.janela = Toplevel()
    self.janela.title("Novo User")
    self.janela.configure(bg= "#D9D9D9")
    self.janela.geometry("500x400") # Largura x Altura
    self.janela.resizable(False, False)          #RESPONSIVIDADE
    self.janela.focus_force()
    self.janela.grab_set()


# ----------- BOTÕES ----------- 
    self.btCriar = Button(
        self.janela,
        bg= "#2EC27B",
        fg= "#FFFFFF",
        text="Criar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command= lambda: adicionarNovoUser(self)
    )
    self.btCriar.place(
        relx= 0.6, 
        rely=0.815, 
        width=100, 
        height=45
    )
    
    self.btCancelar = Button(
        self.janela,
        bg= "#C22E2E",
        fg= "#FFFFFF",
        text="Cancelar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command= lambda: self.janela.destroy()

    )
    self.btCancelar.place(
        relx= 0.2, 
        rely=0.815, 
        width=100, 
        height=45
    )


# ----------- LABELS E INPUTS ----------- 
    self.lbNovoLogin = Label(
        self.janela,
        text="Login:",
        bg= "#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"   
    )
    self.lbNovoLogin.place(
        relx= 0.125,
        rely= 0.05
    )
    self.inputNovoLogin = Entry(self.janela, font=50)
    self.inputNovoLogin.place(
        relx=0.5,
        rely = 0.05,
        relwidth=0.4, 
        height=30
    )


    self.lbEmail = Label(
        self.janela,
        text="Email:",
        bg= "#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"   
    )
    self.lbEmail.place(
        relx= 0.125,
        rely= 0.2
    )
    self.inputNovoEmail = Entry(self.janela, font=50)
    self.inputNovoEmail.place(
        relx=0.5,
        rely = 0.2,
        relwidth=0.4, 
        height=30
    )


    self.lbAcesso = Label(
        self.janela,
        text="Acesso:",
        bg= "#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"   
    )
    self.lbAcesso.place(
        relx= 0.125,
        rely= 0.35
    )
    self.selAcesso = ttk.Combobox(
        self.janela, 
        values= ["admin", "bolsista", "tecnico"], 
        state="readonly", 
        width=10,
    )
    self.selAcesso.place(
        relx=0.5, 
        rely = 0.35
    )


    self.lbSenha = Label(
        self.janela,
        text="Senha:",
        bg= "#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"   
    )
    self.lbSenha.place(
        relx= 0.125,
        rely= 0.5
    )  
    self.inputSenha1 = Entry(
        self.janela, 
        font=50,
        show="*"
    )
    self.inputSenha1.place(
        relx=0.5,
        rely = 0.5,
        relwidth=0.4, 
        height=30
    )


    self.lbConfirmSenha = Label(
        self.janela,
        text="Confirmar Senha:",
        bg= "#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"   
    )
    self.lbConfirmSenha.place(
        relx= 0.125,
        rely= 0.65
    )  
    self.inputConfirmSenha = Entry(
        self.janela, 
        font=50,
        show="*"
    )
    self.inputConfirmSenha.place(
        relx=0.5,
        rely = 0.65,
        relwidth=0.4, 
        height=30
    )