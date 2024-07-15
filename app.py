from modulos import *
from gerenciar import *
from buscar import *
from historico import *
from imprimir import *

# ----------- JANELA -----------
class App(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Sistema de Inventário")
        self.configure(bg="#29273A")
        self.geometry("1200x900")  # Largura x Altura
        self.resizable(False, False)  # RESPONSIVIDADE
        #self.maxsize(width="", heigth="")  #TAMANHO MÁXIMO 
        #self.minsize(width="", heigth="")  #TAMANHO MÍNIMO

        id(self)
        menu(self)
        gerenciar(self)
        buscar(self)
        historico(self)
        imprimir(self)

# ----------- LOGO E NOME SISTEMA -----------
def id(self):
    titulo = tk.Label(
        self,
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

    ass = tk.Label(
        self,
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
    img = Image.open(imagem_path)
    img = img.resize((187, 100), Image.ANTIALIAS)  # Largura x Altura
    img = ImageTk.PhotoImage(img)

    # Adicionar a img ao widget Label
    self.labelImagem = Label(
        self, 
        image=img, 
        bg="#29273A"
    )
    self.labelImagem.img = img  # Mantém uma referência para evitar que a imagem seja coletada pelo garbage collector
    self.labelImagem.place(
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
