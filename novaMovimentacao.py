from modulos import *
from funcoes.funcNovaMov import *

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

# ----------- BOTÕES ----------- 
    self.btNovoHist = Button(
        self.novoHist,
        bg= "#2EC27B",
        fg= "#FFFFFF",
        text="Criar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command= lambda: funcBtNovoHist(self)
    )
    self.btNovoHist.place(
        relx= 0.6, 
        rely=0.815, 
        width=100, 
        height=45
    )
    
    self.btCancelarHist = Button(
        self.novoHist,
        bg= "#C22E2E",
        fg= "#FFFFFF",
        text="Cancelar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command= lambda: funcBtCancelarHist(self)

    )
    self.btCancelarHist.place(
        relx= 0.2, 
        rely=0.815, 
        width=100, 
        height=45
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
        rely= 0.075
    )
    self.inputTomboNovHist = Entry(self.novoHist, font=50)
    self.inputTomboNovHist.place(
        relx=0.5,
        rely = 0.075,
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
        rely= 0.25
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
        rely = 0.25
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
        rely= 0.45
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
        rely = 0.45
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
        rely= 0.65
    )        
    responsaveis = ["Eu", "Tú", "Ele"]  # Lista de responsáveis
    self.selResponsavel = ttk.Combobox(
        self.novoHist, 
        values=responsaveis, 
        state="readonly", 
        width=10,
    )
    self.selResponsavel.place(
        relx=0.5, 
        rely = 0.65
    )