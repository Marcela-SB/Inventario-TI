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
        self.historico()
        self.imprimir()
        #self.checkbox()
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

        ass = Label(
            anchor="nw",
            text="M - F - V",
            fg= "#D9D9D9",
            bg= "#29273A",
            font=("Inter Black", 10 * -1, "bold")
        )
        ass.place(
            relx= 0.945,
            rely= 0.975
        )


        # Carregar a imagem
        imagem_path = os.path.join(os.path.dirname(__file__), "imagens/ufrn.png")
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
        self.aba_imprimir = tk.Frame(self.notebook, bg="#D9D9D9")

        # Add frames to notebook (tab container)
        self.notebook.add(self.aba_gerenciar, text="Gerenciar")
        self.notebook.add(self.aba_buscar, text="Buscar")
        self.notebook.add(self.aba_historico, text="Histórico")
        self.notebook.add(self.aba_imprimir, text="Impressão")

        # CONTEÚDOS DAS ABAS
        tk.Label(self.aba_gerenciar, bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_buscar, bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_historico, bg="#D9D9D9").pack(pady=20)
        tk.Label(self.aba_imprimir, bg="#D9D9D9").pack(pady=20)

        style = ttk.Style()
        # Configurando o estilo para as abas do notebook
        style.configure('EstiloAbas.TNotebook.Tab', font=('Inter Regular', 20), padding=[20, 10])

        # Ajustando a largura e altura das abas (SELECIONADAS OU NÃO)
        style.map('EstiloAbas.TNotebook.Tab', 
              width=[('selected', 150), ('!selected', 100)], 
              height=[('selected', 50), ('!selected', 45)])

        # Aplicando o estilo ao notebook
        self.notebook.configure(style='EstiloAbas.TNotebook')


#/////////////////////////////////////////////////
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
        self.inputTombo = Entry(self.aba_gerenciar, font=50)
        self.inputTombo.place(
            relx = 0.25,
            rely = 0.05,
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
            rely = 0.125
        )
        self.inputItem = Entry(self.aba_gerenciar, font=50)
        self.inputItem.place(
            relx = 0.25,
            rely = 0.127,
            relwidth=0.4, 
            height=30
        )

        self.lbDescricao = Label(           # DESCRIÇÃO
            self.aba_gerenciar, 
            text="Descricao:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbDescricao.place(
            relx = 0.05,
            rely = 0.21
        )
        self.inputDescricao = Entry(self.aba_gerenciar, font=50)
        self.inputDescricao.place(
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
            font=50,
            state="readonly", 
            width=10
        )
        self.combobox.place(
            relx=0.25, 
            rely = 0.31
        )
        style = ttk.Style()
        style.configure('TCombobox', padding=(10, 5, 10, 5), arrowsize=15)


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
        self.inputExcluir = Entry(self.aba_gerenciar, font=50)
        self.inputExcluir.place(
            relx = 0.25,
            rely = 0.71,
            relwidth=0.4, 
            height=30,
        )


    def buscar(self):
# ----------- LABELS E INPUTS ----------- 
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
        self.inputTombo = Entry(self.aba_buscar, font=50)
        self.inputTombo.place(
            relx = 0.25,
            rely = 0.06,
            relwidth=0.4, 
            height=30
        )

        self.lbItem = Label(           # ITEM
            self.aba_buscar, 
            text="Item:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbItem.place(
            relx = 0.05,
            rely = 0.125
        )
        self.inputItem = Entry(self.aba_buscar, font=50)
        self.inputItem.place(
            relx = 0.25,
            rely = 0.127,
            relwidth=0.4, 
            height=30
        )

        self.lbSala = Label(           # SALA
            self.aba_buscar, 
            text="Sala:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbSala.place(
            relx = 0.05,
            rely = 0.21
        )

                                                # LISTA SUSPENSA
        numeros = [str(i) for i in range(1, 49)]  # Lista de números de 1 a 48
        self.combobox = ttk.Combobox(
            self.aba_buscar, 
            values=numeros, 
            state="readonly", 
            width=10,
        )
        self.combobox.place(
            relx=0.25, 
            rely = 0.21
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
        # "DIV"
        self.areaBusca = Frame(self.aba_buscar, bg="#D9D9D9")
        self.areaBusca.place(
            relx= 0.02, 
            rely=0.3, 
            relwidth=0.95, 
            relheight=0.67
        )

        # COLUNAS
        self.lista = ttk.Treeview(
            self.areaBusca,
            height = 3,
            column=("col1", "col2", "col3", "col4", "col5")
        )
        self.lista.heading("#1", text="TOMBO")
        self.lista.heading("#2", text="ITEM")
        self.lista.heading("#3", text="DETALHAMENTO")
        self.lista.heading("#4", text="LOCALIZAÇÃO")
        self.lista.heading("#5", text="STATUS")

        self.lista.column("#0", width=2)

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
        self.scroolLista.config(command=self.lista.yview)
        self.scroolLista.place(
            relx=0.98,
            rely=0.00001, 
            relwidth=0.02, 
            relheight=1
        )


    def historico(self):
# ----------- LABELS E INPUTS ----------- 
        self.lbTombo = Label(           # TOMBO
            self.aba_historico, 
            text="Tombo:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbTombo.place(
            relx = 0.05,
            rely = 0.08
        )
        self.inputTombo = Entry(self.aba_historico, font=50)
        self.inputTombo.place(
            relx = 0.15,
            rely = 0.08,
            relwidth=0.4, 
            height=30
        )

# ----------- BOTÕES -----------         
        self.btNovo = Button(
            self.aba_historico,
            bg= "#2EC27B",
            fg= "#FFFFFF",
            text="Novo",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command= self.criarNovoHistorico
        )
        self.btNovo.place(
            relx= 0.8, 
            rely=0.055, 
            width=180, 
            height=61
        )

        
        self.btBuscar = Button(
            self.aba_historico,
            bg= "#347deb",
            fg= "#FFFFFF",
            text="Buscar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Buscar")
        )
        self.btBuscar.place(
            relx= 0.62, 
            rely=0.055, 
            width=180, 
            height=61
        )


# ----------- TABELA DE HISTÓRICO -----------  
        # "DIV"
        self.areaHistorico = Frame(self.aba_historico, bg="#D9D9D9")
        self.areaHistorico.place(
            relx= 0.02, 
            rely=0.205, 
            relwidth=0.95, 
            relheight=0.78
        )

        # COLUNAS
        self.entradas = ttk.Treeview(
            self.areaHistorico,
            height = 3,
            column=("col1", "col2", "col3", "col4")
        )
        self.entradas.heading("#1", text="DATA/HORA DA OPERAÇÃO")
        self.entradas.heading("#2", text="ORIGEM")
        self.entradas.heading("#3", text="DESTINO")
        self.entradas.heading("#4", text="RESPONSÁVEL")

        self.entradas.column("#0", width=0, stretch=tk.NO)

        self.entradas.place(
            relx= 0.0, 
            rely=0.0, 
            relwidth=0.98, 
            relheight=1
        )

        self.scroolEntradas = Scrollbar(
            self.areaHistorico,
            orient="vertical"
        )
        self.entradas.configure(yscrollcommand= self.scroolEntradas.set)
        self.scroolEntradas.config(command=self.entradas.yview)
        self.scroolEntradas.place(
            relx=0.98,
            rely=0.00001, 
            relwidth=0.02, 
            relheight=1
        )

    def criarNovoHistorico(self):
        self.janelinha = Toplevel()
        self.janelinha.title("Novo Histórico")
        self.janelinha.configure(bg= "#29273A")
        self.janelinha.geometry("500x400") # Largura x Altura
        self.janelinha.resizable(False, False)          #RESPONSIVIDADE
        self.janelinha.focus_force()
        self.janelinha.grab_set()

        self.novoHist = Frame(
            self.janelinha,
            bg= "#D9D9D9"
        )
        self.novoHist.place(
            relx= 0.05,
            rely= 0.05,
            relwidth= 0.9,
            relheight= 0.9
        )

# ----------- LABELS E INPUTS ----------- 
        self.histTombo = Label(
            self.novoHist,
            text="Tombo:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.histTombo.place(
            relx= 0.125,
            rely= 0.1
        )
        self.inputTombo = Entry(self.novoHist, font=50)
        self.inputTombo.place(
            relx=0.5,
            rely = 0.1,
            relwidth=0.4, 
            height=30
        )


        self.origem = Label(
            self.novoHist,
            text="Origem:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.origem.place(
            relx= 0.15,
            rely= 0.3
        )
        numeros = [str(i) for i in range(1, 49)]  # Lista de números de 1 a 48
        self.selOrigem = ttk.Combobox(
            self.novoHist, 
            values=numeros, 
            state="readonly", 
            width=10,
        )
        self.selOrigem.place(
            relx=0.5, 
            rely = 0.3
        )


        self.destino = Label(
            self.novoHist,
            text="Destino:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.destino.place(
            relx= 0.15,
            rely= 0.5
        )
        numeros = [str(i) for i in range(1, 49)]  # Lista de números de 1 a 48
        self.selDestino = ttk.Combobox(
            self.novoHist, 
            values=numeros, 
            state="readonly", 
            width=10,
        )
        self.selDestino.place(
            relx=0.5, 
            rely = 0.5
        )


        self.histRespons = Label(
            self.novoHist,
            text="Responsável:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.histRespons.place(
            relx= 0.125,
            rely= 0.7
        )        
        responsaveis = ["Eu", "Tú", "Ele"]  # Lista de responsáveis
        self.selDestino = ttk.Combobox(
            self.novoHist, 
            values=responsaveis, 
            state="readonly", 
            width=10,
        )
        self.selDestino.place(
            relx=0.5, 
            rely = 0.7
        )






    def imprimir(self):       
        self.separator = Frame(         # SEPARADOR
            self.aba_imprimir, 
            bg="#9B9B9B", 
            width=2, 
            bd=0
         )
        self.separator.place(
            relx=0.7, 
            rely=0.45, 
            relheight=0.5) 


# ----------- LABELS E INPUTS ----------- 
        self.legenda = Label(
            self.aba_imprimir, 
            text="Selecione o que deseja imprimir do item acima:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.legenda.place(
            relx = 0.05,
            rely = 0.5
        )

        self.extras = Label(
            self.aba_imprimir, 
            text="Extras:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.extras.place(
            relx = 0.75,
            rely = 0.5
        )

        self.conferir = Label(
            self.aba_imprimir, 
            text="Confira o item inserido acima:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.conferir.place(
            relx = 0.05,
            rely = 0.2
        )

        self.lbTombo = Label(           # TOMBO
            self.aba_imprimir, 
            text="Tombo:", 
            bg="#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"                     
        )
        self.lbTombo.place(
            relx = 0.05,
            rely = 0.05
        )
        self.inputTombo = Entry(self.aba_imprimir, font=50)
        self.inputTombo.place(
            relx = 0.25,
            rely = 0.05,
            relwidth=0.4, 
            height=30
        )

# ----------- BOTÕES -----------
        self.btQRCode = Button(
            self.aba_imprimir,
            bg= "#cc6d2d",
            fg= "#FFFFFF",
            text="QR Code",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("QR Code")
        )
        self.btQRCode.place(
            relx= 0.15, 
            rely=0.8, 
            width=180, 
            height=61
        )

        self.btCodigoBarras = Button(
            self.aba_imprimir,
            bg= "#cc6d2d",
            fg= "#FFFFFF",
            text="Cód. de Barras",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Detalhes")
        )
        self.btCodigoBarras.place(
            relx= 0.4, 
            rely=0.8, 
            width=180, 
            height=61
        )

        self.btImpHist = Button(
            self.aba_imprimir,
            bg= "#cc6d2d",
            fg= "#FFFFFF",
            text="Histórico",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Histórico")
        )
        self.btImpHist.place(
            relx= 0.15, 
            rely=0.65, 
            width=180, 
            height=61
        )

        self.btImpDetal = Button(
            self.aba_imprimir,
            bg= "#cc6d2d",
            fg= "#FFFFFF",
            text="Detalhes Item",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Detalhes")
        )
        self.btImpDetal.place(
            relx= 0.4, 
            rely=0.65, 
            width=180, 
            height=61
        )

        self.btInventario = Button(
            self.aba_imprimir,
            bg= "#cc6d2d",
            fg= "#FFFFFF",
            text="Imprimir\nInventário\nCompleto",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Imprimir")
        )
        self.btInventario.place(
            relx= 0.8, 
            rely=0.7, 
            width=180, 
            height=101
        )

# ----------- CONFERIR ITEM -----------  
        # "DIV"
        self.areaConferir = Frame(self.aba_imprimir, bg="#D9D9D9")
        self.areaConferir.place(
            relx= 0.02, 
            rely=0.25, 
            relwidth=0.95, 
            relheight=0.1
        )

        # COLUNAS
        self.conferindo = ttk.Treeview(
            self.areaConferir,
            height = 3,
            column=("col1", "col2", "col3", "col4", "col5")
        )
        self.conferindo.heading("#1", text="TOMBO")
        self.conferindo.heading("#2", text="ITEM")
        self.conferindo.heading("#3", text="DETALHAMENTO")
        self.conferindo.heading("#4", text="LOCALIZAÇÃO")
        self.conferindo.heading("#5", text="STATUS")

        self.conferindo.column("#0", width=0, stretch=tk.NO)

        self.conferindo.place(
            relx= 0.0, 
            rely=0.0, 
            relwidth=1, 
            relheight=1
        )

    
    """def checkbox(self):
        self.checkInfo = ttk.Button(
            self.aba_imprimir, 
            text="Informações Item", 
            style="Custom.TButton",
            command=self.on_button_click
        )
        self.checkInfo.pack(pady=40)    

        '''self.checkInfo = Button(
            self.aba_imprimir,
            text="Informações Item",
            bg="red",
            fg= "#FFFFFF",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: print("Info")
        )
        self.checkInfo.place(
            relx= 0.5,
            rely= 0.8
        )'''

        self.button_toggled = False
        
        # Cria uma instância de ttk.Style
        style = ttk.Style(self)
        
        # Define estilo para o estado normal do botão
        style.configure(
            "Custom.TButton",
            font=("Inter Regular", 18 * -1),
            foreground="red",
            background="yellow",
            padding=10
        )
        
        # Define estilo para o estado pressionado do botão
        style.map(
            "Custom.TButton",
            foreground=[("pressed", "white"), ("active", "white")],
            background=[("pressed", "#005F8C"), ("active", "#005F8C")]
        )

        # Define estilo para o botão alternado
        style.configure(
            "Toggled.TButton",
            font=("Arial", 14),
            foreground="blue",
            background="pink",  # Cor diferente para o estado alternado
            padding=10
        )
        
        # Adiciona um botão com o estilo personalizado
        
    
    def on_button_click(self):
        # Alterna o estado do botão
        self.button_toggled = not self.button_toggled
        
        # Altera o estilo do botão baseado no estado
        if self.button_toggled:
            self.checkInfo.configure(style="Toggled.TButton")
        else:
            self.checkInfo.configure(style="Custom.TButton")
        
        print("Botão clicado! Estado:", self.button_toggled)"""

Application()
