from modulos import *
from funcoes.funcEsqueciSenha import *

def mudarSenha(self):
    self.janelaEsqueciSenha = Toplevel()
    self.janelaEsqueciSenha.title("Atualizar senha")
    self.janelaEsqueciSenha.configure(bg= "#D9D9D9")
    self.janelaEsqueciSenha.geometry("500x200") # Largura x Altura
    self.janelaEsqueciSenha.resizable(False, False)          #RESPONSIVIDADE
    self.janelaEsqueciSenha.focus_force()
    self.janelaEsqueciSenha.grab_set()


# ----------- BOTÕES ----------- 
    self.btAtualizarSenha = Button(
        self.janelaEsqueciSenha,
        bg= "#2EC27B",
        fg= "#FFFFFF",
        text="Atualizar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command= lambda: esqueciSenha(self)
    )
    self.btAtualizarSenha.place(
        relx= 0.6, 
        rely=0.7, 
        width=120, 
        height=45
    )
    # função para acionar botão "ATUALIZAR" ao apertar "ENTER"
    self.janelaEsqueciSenha.bind('<Return>', lambda event:  esqueciSenha(self))
    
    self.btCancelar = Button(
        self.janelaEsqueciSenha,
        bg= "#C22E2E",
        fg= "#FFFFFF",
        text="Cancelar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command= lambda: self.janelaEsqueciSenha.destroy()

    )
    self.btCancelar.place(
        relx= 0.2, 
        rely=0.7, 
        width=120, 
        height=45
    )


# ----------- LABELS E INPUTS ----------- 
    self.lbEmailEsqSen = Label( 
        self.janelaEsqueciSenha, 
        text="Email:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbEmailEsqSen.place(
        relx = 0.07,
        rely = 0.12
    )
    self.inputEmailEsqSen = Entry(self.janelaEsqueciSenha, font=50)
    self.inputEmailEsqSen.place(
        relx = 0.35,
        rely = 0.12,
        relwidth=0.58, 
        height=30
    )

    self.lbAtualizarSenha = Label( 
        self.janelaEsqueciSenha, 
        text="Nova Senha:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbAtualizarSenha.place(
        relx = 0.07,
        rely = 0.42
    )
    self.inputSenhaEsqSen = Entry(
        self.janelaEsqueciSenha, 
        font=50, 
        show="*"
    )
    self.inputSenhaEsqSen.place(
        relx = 0.35,
        rely = 0.42,
        relwidth=0.58, 
        height=30
    )