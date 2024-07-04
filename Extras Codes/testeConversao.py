from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.framesDaTela()
        self.criandoBotoes()
        self.objetos()
        root.mainloop()

    def tela(self):
        self.root.title("Sistema de Inventário")
        self.root.configure(bg= "#29273A")
        self.root.geometry("1440x1000")
        self.root.resizable(False, False)

    def framesDaTela(self):
        self.frame_titulo = Frame(
            self.root, 
            bg="#29273A",
            highlightbackground="#9B9B9B",
            highlightthickness= 0
        )
        self.frame_titulo.place(
            relx=0, 
            rely=0, 
            relwidth=1, 
            relheight=0.1
        )

        self.lbTitulo = Label(
            self.frame_titulo, 
            text="Sistema de Inventário",
            bg="#29273A",
            font=("Ivy 20 bold"), 
            fg= "white"                     
        )
        self.lbTitulo.place(
            relx = 0.5,
            rely = 0.5,
            anchor="center"
        )

        self.frame_menu = Frame(
            self.root, 
            bg="#29273A",
            highlightbackground="#9B9B9B",
            highlightthickness= 0
        )
        self.frame_menu.place(
            relx=0, 
            rely=0.1, 
            relwidth=1, 
            relheight=0.1
        )

        self.btMenu1 = Button(
            self.frame_menu, 
            text="Opção 1",
            bg="#29273A",
            font=("Ivy 10 bold"), 
            fg= "white",
            bd=0
        )
        self.btMenu1.place(
            relx = 0.1,
            rely = 0.5,
            anchor="center"
        )

        self.btMenu2 = Button(
            self.frame_menu, 
            text="Opção 2",
            bg="#29273A",
            font=("Ivy 10 bold"), 
            fg= "white",
            bd=0
        )
        self.btMenu2.place(
            relx = 0.3,
            rely = 0.5,
            anchor="center"
        )

        self.btMenu3 = Button(
            self.frame_menu, 
            text="Opção 3",
            bg="#29273A",
            font=("Ivy 10 bold"), 
            fg= "white",
            bd=0
        )
        self.btMenu3.place(
            relx = 0.5,
            rely = 0.5,
            anchor="center"
        )

        self.btMenu4 = Button(
            self.frame_menu, 
            text="Opção 4",
            bg="#29273A",
            font=("Ivy 10 bold"), 
            fg= "white",
            bd=0
        )
        self.btMenu4.place(
            relx = 0.7,
            rely = 0.5,
            anchor="center"
        )

        self.frame_principal = Frame(
            self.root, 
            bd=4, 
            bg="#D9D9D9",
            highlightbackground="#9B9B9B",
            highlightthickness= 1.5
        )
        self.frame_principal.place(
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
            relx= 0.8, 
            rely=0.8, 
            relwidth=0.1, 
            relheight=0.15
        )

    def objetos(self):
        self.lbTombo = Label(
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

        self.lbItem = Label(
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

        self.lbSala = Label(
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
