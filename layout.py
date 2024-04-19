from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.framesDaTela()
        self.criandoBotoes()
        root.mainloop()

    def tela(self):
        self.root.title("Sistema de Inventário")
        self.root.configure(bg= "#29273A")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        #self.root.maxsize(width="", heigth="")  #TAMANHO MÁXIMO 
        #self.root.minsize(width="", heigth="")  #TAMANHO MÍNIMO

    def framesDaTela(self):
# FRAME PRINCIPAL
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
    
    def criandoBotoes(self):
        self.btBuscar = Button(
            self.frame_principal, 
            text="Buscar"
        )

        self.btBuscar.place(
            relx= 0.1, 
            rely=0.2, 
            relwidth=0.1, 
            relheight=0.15
        )



Application()
