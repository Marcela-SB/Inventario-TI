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
        '''self.frameDaTela()'''
        self.id()
        self.menu()
        self.gerenciar()
        self.buscar()
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
    def menu(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.place(
            x=28.0,
            y=120.0,
            width=1150.0,
            height=750.0
        )

        # CRIANDO FRAMES PARA CADA ABA
        self.aba_gerenciar = tk.Frame(self.notebook, bg="#D9D9D9")
        self.aba_buscar = tk.Frame(self.notebook, bg="#D9D9D9")
        self.aba_historico = tk.Frame(self.notebook, bg="#D9D9D9")
        self.aba_impressao = tk.Frame(self.notebook, bg="#D9D9D9")

        # Add frames to notebook (tab container)
        self.notebook.add(self.aba_gerenciar, text="Gerenciar")
        self.notebook.add(self.aba_buscar, text="Buscar")
        self.notebook.add(self.aba_historico, text="Histórico")
        self.notebook.add(self.aba_impressao, text="Impressão")

        # CONTEÚDOS DAS ABAS
        tk.Label(self.aba_gerenciar, bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_buscar, text="Buscar Conteúdo", bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_historico, text="Histórico Conteúdo", bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_impressao, text="Impressão Conteúdo", bg="#D9D9D9").pack(pady=20)

        style = ttk.Style()
        # Configurando o estilo para as abas do notebook
        style.configure('EstiloAbas.TNotebook.Tab', font=('Inter Regular', 20), padding=[20, 10])

        # Ajustando a largura e altura das abas (SELECIONADAS OU NÃO)
        style.map('EstiloAbas.TNotebook.Tab', 
              width=[('selected', 150), ('!selected', 100)], 
              height=[('selected', 50), ('!selected', 45)])

        # Aplicando o estilo ao notebook
        self.notebook.configure(style='EstiloAbas.TNotebook')


    def gerenciar(self):
        
        self.separator = Frame(         # SEPARADOR
            self.aba_gerenciar, 
            bg="#9B9B9B", 
            height=2, 
            bd=0
         )
        self.separator.place(
            relx=0.01, 
            rely=0.55, 
            relwidth=0.98) 


# ----------- BOTÕES -----------         
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


    def buscar(self):
        self.lbTombo = Label(           # TOMBO
            self.aba_buscar, 
            text="Tombo:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbTombo.place(
            relx = 0.05,
            rely = 0.05
        )
        self.inputTombo = Entry(self.aba_buscar)
        self.inputTombo.place(
            relx = 0.25,
            rely = 0.06,
            relwidth=0.4, 
            height=30
        )

# ----------- BOTÕES -----------         
        self.btBuscar = Button(
            self.aba_buscar,
            bg= "#347deb",
            fg= "#FFFFFF",
            text="Buscar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Buscar")
        )
        self.btBuscar.place(
            relx= 0.8, 
            rely=0.04, 
            width=180, 
            height=61
        )

# ----------- TABELA DE BUSCA -----------  
        self.areaBusca = Frame(self.aba_buscar, bg="#D9D9D9")
        self.areaBusca.place(
            relx= 0.02, 
            rely=0.205, 
            relwidth=0.95, 
            relheight=0.78
        )

        # COLUNAS
        self.lista = ttk.Treeview(
            self.areaBusca,
            height = 3,
            column=("col1", "col2", "col3")
        )
        self.lista.heading("#1", text="TOMBO")
        self.lista.heading("#2", text="ITEM")
        self.lista.heading("#3", text="LOCALIZAÇÃO")

        self.lista.column("#0", width=0, stretch=tk.NO)

        self.lista.place(
            relx= 0.0, 
            rely=0.0, 
            relwidth=0.98, 
            relheight=1
        )

        self.scroolLista = Scrollbar(
            self.areaBusca,
            orient="vertical"
        )
        self.lista.configure(yscrollcommand= self.scroolLista.set)
        self.scroolLista.place(
            relx=0.98,
            rely=0.00001, 
            relwidth=0.02, 
            relheight=1
        )

Application()
