# ARQUIVOS DA MODULARIZAÇÃO
from modulos import *
from conexaoBD import*
from gerenciar import *
from buscar import *
from historico import *
from imprimir import *


class Application(tk.Tk):
# ----------- INICIALIZAÇÃO -----------
    def __init__(self):
        super().__init__()
        self.tela()
        '''self.frameDaTela()'''
        self.id()
        self.menu()
        gerenciar(self)
        buscar(self)
        historico(self)
        imprimir(self)
        #self.checkbox()
        self.mainloop()

        '''def chamarConexao(self):
        iniciar = None
        while(iniciar == None):
            iniciar = conectar_bd(self)'''

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


        '''# Carregar a imagem
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
        )'''


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