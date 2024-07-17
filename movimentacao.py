from modulos import *
from novaMovimentacao import *
from funcoes.funcMov import *

def movimentacao(self):
# ----------- LABELS E INPUTS ----------- 
    self.lbTomboMov = Label(           # TOMBO
        self.aba_movimentacao, 
        text="Tombo:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbTomboMov.place(
        relx = 0.05,
        rely = 0.08
    )
    self.inputTomboMov = Entry(self.aba_movimentacao, font=50)
    self.inputTomboMov.place(
        relx = 0.15,
        rely = 0.08,
        relwidth=0.4, 
        height=30
    )

# ----------- BOTÕES -----------         
    self.btNovaMov = Button(
        self.aba_movimentacao,
        bg= "#2EC27B",
        fg= "#FFFFFF",
        text="Novo",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: criarNovaMovimentacao(self)
    )
    self.btNovaMov.place(
        relx= 0.8, 
        rely=0.055, 
        width=180, 
        height=61
    )

    
    self.btBuscarMov = Button(
        self.aba_movimentacao,
        bg= "#347deb",
        fg= "#FFFFFF",
        text="Buscar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcbtBuscarMov(self)
    )
    self.btBuscarMov.place(
        relx= 0.62, 
        rely=0.055, 
        width=180, 
        height=61
    )


# ----------- TABELA DE MovÓRICO -----------  
    # "DIV"
    self.areamovimentacao = Frame(self.aba_movimentacao, bg="#D9D9D9")
    self.areamovimentacao.place(
        relx= 0.02, 
        rely=0.205, 
        relwidth=0.95, 
        relheight=0.78
    )

    # COLUNAS
    self.entradas = ttk.Treeview(
        self.areamovimentacao,
        height = 3,
        column=("col1", "col2", "col3", "col4")
    )
    self.entradas.heading("#0", text="#")
    self.entradas.heading("#1", text="DATA/HORA DA OPERAÇÃO")
    self.entradas.heading("#2", text="ORIGEM")
    self.entradas.heading("#3", text="DESTINO")
    self.entradas.heading("#4", text="RESPONSÁVEL")

    self.entradas.column("#0", width=2)

    self.entradas.place(
        relx= 0.0, 
        rely=0.0, 
        relwidth=0.98, 
        relheight=1
    )

    self.scroolEntradas = Scrollbar(
        self.areamovimentacao,
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