from tkinter import *

root = Tk()

class Application():
# ----------- INICIALIZAÇÃO -----------
    def __init__(self):
        self.root = root
        self.tela()
        self.framesDaTela()
        self.criandoBotoes()
        self.objetos()
        root.mainloop()

# ----------- JANELA -----------
    def tela(self):
        self.root.title("Sistema de Inventário")
        self.root.configure(bg= "#29273A")
        self.root.geometry("1440x1000")
        self.root.resizable(False, False)          #RESPONSIVIDADE
        #self.root.maxsize(width="", heigth="")  #TAMANHO MÁXIMO 
        #self.root.minsize(width="", heigth="")  #TAMANHO MÍNIMO
        
# ----------- FRAME PRINCIPAL -----------

# ----------- FRAME PRINCIPAL -----------
    def framesDaTela(self):
        self.frame_principal = Frame(       # DETALHES DO FRAME PRINCIPAL
            self.root, 
            bd=4, 
            bg="#D9D9D9",
            highlightbackground="#9B9B9B",
            highlightthickness= 1.5
        )
        self.frame_principal.place(         # POSIÇÃO (relativa) DO FRAME PRINCIPAL
            relx= 0.01, 
            rely=0.2, 
            relwidth=0.98, 
            relheight=0.78
        )




# ----------- BOTÕES ----------- 
    def criandoBotoes(self):
        self.btBuscar = Button(
            self.frame_principal, 
            text="Buscar"
        )

        self.btBuscar.place(
            relx= 0.8, 
            rely=0.8, 
            relwidth=0.1, 
            relheight=0.15
        )

# ----------- LABELS E INPUTS ----------- 
    def objetos(self):
        self.lbTombo = Label(           # TOMBO
            self.frame_principal, 
            text="Tombo:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbTombo.place(
            relx = 0.05,
            rely = 0.05
        )
        self.inputTombo = Entry(self.frame_principal)
        self.inputTombo.place(
            relx = 0.25,
            rely = 0.06,
            relwidth=0.4, 
            height=30
        )

        self.lbItem = Label(           # ITEM
            self.frame_principal, 
            text="Item:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbItem.place(
            relx = 0.05,
            rely = 0.2
        )
        self.inputItem = Entry(self.frame_principal)
        self.inputItem.place(
            relx = 0.25,
            rely = 0.21,
            relwidth=0.4, 
            height=30
        )

        self.lbSala = Label(           # SALA
            self.frame_principal, 
            text="Sala:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbSala.place(
            relx = 0.05,
            rely = 0.3
        )
        self.inputSala = Entry(self.frame_principal)
        self.inputSala.place(
            relx = 0.25,
            rely = 0.31,
            relwidth=0.4, 
            height=30
        )


Application()
