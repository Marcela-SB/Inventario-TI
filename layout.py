import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os


class Application(tk.Tk):
# ----------- INICIALIZAÇÃO -----------
    def __init__(self):
        super().__init__()
        self.tela()
        self.frameDaTela()
        self.id()
        self.menu()
        self.abas_test()
        self.criandoBotoes()
        self.objetos()
        self.mainloop()

# ----------- JANELA -----------
    def tela(self):
        self.title("Sistema de Inventário")
        self.configure(bg= "#29273A")
        self.geometry("1200x900") # Largura x Altura
        self.resizable(False, False)          #RESPONSIVIDADE
        #self.maxsize(width="", heigth="")  #TAMANHO MÁXIMO 
        #self.minsize(width="", heigth="")  #TAMANHO MÍNIMO
        
# ----------- FRAME PRINCIPAL -----------
    def frameDaTela(self):
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
        )

        self.separator = Frame(         # CONTORNO DO FRAME PRINCIPAL
            self.frame_principal, 
            bg="#9B9B9B", 
            height=2, 
            bd=0
         )
        self.separator.place(
            relx=0.01, 
            rely=0.55, 
            relwidth=0.98)        


# ----------- LOGO E NOME SISTEMA -----------
    def id(self):
        titulo = Label(
            anchor="nw",
            text="Inventário T.I. DEART",
            fg= "#D9D9D9",
            bg= "#29273A",
            font=("Inter Black", 40 * -1, "bold")
        )
        titulo.place(
            x= 12.0,
            y= 36.0
        )

        # Carregar a imagem
        imagem_path = os.path.join(os.path.dirname(__file__), "ufrn.png")
        imagem = Image.open(imagem_path)
        imagem = imagem.resize((187, 100), Image.ANTIALIAS)  # Largura x Altura
        imagem = ImageTk.PhotoImage(imagem)

        # Adicionar a imagem ao widget Label
        self.label_imagem = Label(
            self, 
            image=imagem, 
            bg="#29273A"
        )
        self.label_imagem.imagem = imagem  # Mantém uma referência para evitar que a imagem seja coletada pelo garbage collector
        self.label_imagem.place(
            relx=0.82, 
            rely=0.01
        )


# ----------- ABAS MENU -----------
    def id(self):
        titulo = Label(
            anchor="nw",
            text="Inventário T.I. DEART",
            fg= "#D9D9D9",
            bg= "#29273A",
            font=("Inter Black", 40 * -1, "bold")
        )
        titulo.place(
            x= 12.0,
            y= 36.0
        )

        # Carregar a imagem
        imagem_path = os.path.join(os.path.dirname(__file__), "ufrn.png")
        imagem = Image.open(imagem_path)
        imagem = imagem.resize((187, 100), Image.ANTIALIAS)  # Largura x Altura
        imagem = ImageTk.PhotoImage(imagem)

        # Adicionar a imagem ao widget Label
        self.label_imagem = Label(
            self.root, 
            image=imagem, 
            bg="#29273A"
        )
        self.label_imagem.imagem = imagem  # Mantém uma referência para evitar que a imagem seja coletada pelo garbage collector
        self.label_imagem.place(
            relx=0.82, 
            rely=0.01
        )


# ----------- ABAS MENU -----------
    def menu(self):

        aba_1 = Button( 
            bg="#D9D9D9",
            text = 'Gerenciar', 
            font= ("Inter Regular", 20 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_1 clicked (gerenciar)"),
            relief="flat"
        )

        aba_1.place(  
            x=28.0,
            y=120.0, #139
            width=224.0,
            height=81.0

        )

        aba_2 = Button( 
            bg="#D9D9D9",
            text = 'Procurar',
            font= ("Inter Regular", 20 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_2 clicked (procurar)"),
            relief="flat"
        )
        aba_2.place(
            x=287.0,
            y=120.0,
            width=224.0,
            height=81.0
        )

        aba_3 = Button( 
            bg="#D9D9D9",
            text = 'Histórico',
            font= ("Inter Regular", 20 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_3 clicked (histórico)"),
            relief="flat"
        )
        aba_3.place(
            x=546.0,
            y=120.0,
            width=224.0,
            height=81.0
        )


        aba_4 = Button( 
            bg="#D9D9D9",
            text = 'Impressão',
            font= ("Inter Regular", 20 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("aba_4 clicked (impressão)"),
            relief="flat"
        )
        aba_4.place(
            x=805.0,
            y=120.0,
            width=224.0,
            height=81.0
        )

        
    def abas_test(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.place(
            x=28.0,
            y=120.0,
            width=1150.0,
            height=650.0
        )

        # Create frames for each tab
        self.aba_gerenciar = tk.Frame(self.notebook, bg="#D9D9D9")
        self.aba_procurar = tk.Frame(self.notebook, bg="#D9D9D9")
        self.aba_historico = tk.Frame(self.notebook, bg="#D9D9D9")
        self.aba_impressao = tk.Frame(self.notebook, bg="#D9D9D9")

        # Add frames to notebook (tab container)
        self.notebook.add(self.aba_gerenciar, text="Gerenciar")
        self.notebook.add(self.aba_procurar, text="Procurar")
        self.notebook.add(self.aba_historico, text="Histórico")
        self.notebook.add(self.aba_impressao, text="Impressão")

        # Example content for tabs
        tk.Label(self.aba_gerenciar, text="Gerenciar Conteúdo", bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_procurar, text="Procurar Conteúdo", bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_historico, text="Histórico Conteúdo", bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_impressao, text="Impressão Conteúdo", bg="#D9D9D9").pack(pady=20)

        style = ttk.Style()
        # Configurando o estilo para as abas do notebook
        style.configure('EstiloAbas.TNotebook.Tab', font=('Inter Regular', 20))

        # Aplicando o estilo ao notebook
        self.notebook.configure(style='EstiloAbas.TNotebook')

# ----------- BOTÕES ----------- 
    def criandoBotoes(self):
        self.btAdicionar = Button(
            self.aba_gerenciar,
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
            width=180, 
            height=61
        )

        
        self.btExcluir = Button(
            self.aba_gerenciar,
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
            width=180, 
            height=61
        )


# ----------- LABELS E INPUTS ----------- 
    def objetos(self):
        self.lbTombo = Label(           # TOMBO
            self.aba_gerenciar, 
            text="Tombo:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbTombo.place(
            relx = 0.05,
            rely = 0.05
        )
        self.inputTombo = Entry(self.aba_gerenciar)
        self.inputTombo.place(
            relx = 0.25,
            rely = 0.06,
            relwidth=0.4, 
            height=30
        )

        self.lbItem = Label(           # ITEM
            self.aba_gerenciar, 
            text="Item:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbItem.place(
            relx = 0.05,
            rely = 0.2
        )
        self.inputItem = Entry(self.aba_gerenciar)
        self.inputItem.place(
            relx = 0.25,
            rely = 0.21,
            relwidth=0.4, 
            height=30
        )

        self.lbSala = Label(           # SALA
            self.aba_gerenciar, 
            text="Sala:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbSala.place(
            relx = 0.05,
            rely = 0.3
        )

        # LISTA SUSPENSA
        numeros = [str(i) for i in range(1, 49)]  # Lista de números de 1 a 48
        self.combobox = ttk.Combobox(
            self.aba_gerenciar, 
            values=numeros, 
            state="readonly", 
            width=10,
        )
        self.combobox.place(
            relx=0.25, 
            rely = 0.3
        )


        self.lbExcluir = Label(           # EXCLUIR
            self.aba_gerenciar, 
            text="Excluir:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbExcluir.place(
            relx = 0.05,
            rely = 0.71
        )
        self.inputExcluir = Entry(self.aba_gerenciar)
        self.inputExcluir.place(
            relx = 0.25,
            rely = 0.71,
            relwidth=0.4, 
            height=30,
        )

        self.lbExcluir = Label(           # EXCLUIR
            self.frame_principal, 
            text="Excluir:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbExcluir.place(
            relx = 0.05,
            rely = 0.71
        )
        self.inputExcluir = Entry(self.frame_principal)
        self.inputExcluir.place(
            relx = 0.25,
            rely = 0.71,
            relwidth=0.4, 
            height=30,
        )


Application()
