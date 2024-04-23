from tkinter import *

root = Tk()

class Application():
# ----------- INICIALIZAÇÃO -----------
    def __init__(self):
        self.root = root
        self.tela()
        self.framesDaTela()
        self.menu()
        self.criandoBotoes()
        self.objetos()
        root.mainloop()

# ----------- JANELA -----------
    def tela(self):
        self.root.title("Sistema de Inventário")
        self.root.configure(bg= "#29273A")
        self.root.geometry("1200x900") # Largura x Altura
        self.root.resizable(False, False)          #RESPONSIVIDADE
        #self.root.maxsize(width="", heigth="")  #TAMANHO MÁXIMO 
        #self.root.minsize(width="", heigth="")  #TAMANHO MÍNIMO
        
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

        self.separator = Frame(
            self.frame_principal, 
            bg="#9B9B9B", 
            height=2, 
            bd=0
         )
        self.separator.place(
            relx=0.01, 
            rely=0.55, 
            relwidth=0.98)


# ----------- ABAS MENU -----------
    def menu(self):
        aba_1 = Button( 
            bg="#D9D9D9",
            text = 'Gerenciar', 
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_1 clicked (gerenciar)"),
            relief="flat"
        )

        aba_1.place(  
            x=28.0,
            y=139.0,
            width=224.0,
            height=81.0
        )

        aba_2 = Button( 
            bg="#D9D9D9",
            text = 'Procurar',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_2 clicked (procurar)"),
            relief="flat"
        )
        aba_2.place(
            x=287.0,
            y=139.0,
            width=224.0,
            height=81.0
        )

        aba_3 = Button( 
            bg="#D9D9D9",
            text = 'Histórico',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_3 clicked (histórico)"),
            relief="flat"
        )
        aba_3.place(
            x=546.0,
            y=139.0,
            width=224.0,
            height=81.0
        )


        aba_4 = Button( 
            bg="#D9D9D9",
            text = 'Impressão',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_4 clicked (impressão)"),
            relief="flat"
        )
        aba_4.place(
            x=805.0,
            y=139.0,
            width=224.0,
            height=81.0
        )



# ----------- BOTÕES ----------- 
    def criandoBotoes(self):
        self.btAdicionar = Button(
            self.frame_principal,
            bg= "#2EC27B",
            fg= "#FFFFFF",
            text="Adicionar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Adicionar")
        )

        self.btAdicionar.place(
            relx= 0.8, 
            rely=0.4, 
            relwidth=0.1, 
            relheight=0.1
        )

        
        self.btExcluir = Button(
            self.frame_principal,
            bg= "#C22E2E",
            fg= "#FFFFFF",
            text="Excluir",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Excluir")
        )

        self.btExcluir.place(
            relx= 0.8, 
            rely=0.8, 
            relwidth=0.1, 
            relheight=0.1
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
