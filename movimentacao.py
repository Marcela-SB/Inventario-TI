from modulos import *
from novaMovimentacao import *
from funcoes.funcMov import *

def movimentacao(self):
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
        rely = 0.05
    )
    self.inputTomboMov = Entry(self.aba_movimentacao, font=50)
    self.inputTomboMov.place(
        relx = 0.15,
        rely = 0.06,
        relwidth=0.4, 
        height=30
    )

    self.lbDataMov = Label(           # DATA
        self.aba_movimentacao, 
        text="Data:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbDataMov.place(
        relx = 0.05,
        rely = 0.125
    )
    self.inputDataMov = Entry(self.aba_movimentacao, font=50)
    self.inputDataMov.place(
        relx = 0.15,
        rely = 0.127,
        relwidth=0.4, 
        height=30
    )

    self.lbSalaMov = Label(           # SALA
        self.aba_movimentacao, 
        text="Sala:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbSalaMov.place(
        relx = 0.05,
        rely = 0.21
    )

                                            # LISTA SUSPENSA
    numeros = [str(i) for i in range(1, 49)]  # Lista de números de 1 a 48
    self.comboboxMov = ttk.Combobox(
        self.aba_movimentacao, 
        values=numeros, 
        state="readonly", 
        width=10,
    )
    self.comboboxMov.place(
        relx=0.15, 
        rely = 0.21
    )

# ----------- TABELA DE MOVIMENTAÇÃO -----------  
    # "DIV"
    self.areamovimentacao = Frame(self.aba_movimentacao, bg="#D9D9D9")
    self.areamovimentacao.place(
        relx= 0.02, 
        rely=0.3, 
        relwidth=0.95, 
        relheight=0.67
    )

    # COLUNAS
    self.entradas = ttk.Treeview(
        self.areamovimentacao,
        height = 3,
        column=("col1", "col2", "col3", "col4", "col5", "col6", "col7")
    )
    self.entradas.heading("#0", text="#")
    self.entradas.heading("#1", text="TOMBO")
    self.entradas.heading("#2", text="ITEM")
    self.entradas.heading("#3", text="ORIGEM")
    self.entradas.heading("#4", text="DESTINO")
    self.entradas.heading("#5", text="DATA")
    self.entradas.heading("#6", text="HORA")
    self.entradas.heading("#7", text="RESPONSÁVEL")

    # Ajustar largura das colunas
    self.entradas.column("#0", width=40)
    self.entradas.column("col1", width=100, anchor='center', stretch=True)
    self.entradas.column("col2", width=100, anchor='center', stretch=True)
    self.entradas.column("col3", width=80, anchor='center', stretch=True)
    self.entradas.column("col4", width=80, anchor='center', stretch=True)
    self.entradas.column("col5", width=80, anchor='center', stretch=True)
    self.entradas.column("col6", width=80, anchor='center', stretch=True)
    self.entradas.column("col7", width=150, anchor='center', stretch=True)

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