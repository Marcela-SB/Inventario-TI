from modulos import *
from novoHistorico import *
from funcoes.funcHist import *

def historico(self):
# ----------- LABELS E INPUTS ----------- 
    self.lbTomboHist = Label(           # TOMBO
        self.aba_historico, 
        text="Tombo:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbTomboHist.place(
        relx = 0.05,
        rely = 0.08
    )
    self.inputTomboHist = Entry(self.aba_historico, font=50)
    self.inputTomboHist.place(
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
        command=lambda: criarNovoHistorico(self)
    )
    self.btNovo.place(
        relx= 0.8, 
        rely=0.055, 
        width=180, 
        height=61
    )

    
    self.btBuscarHist = Button(
        self.aba_historico,
        bg= "#347deb",
        fg= "#FFFFFF",
        text="Buscar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcbtBuscarHist(self)
    )
    self.btBuscarHist.place(
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