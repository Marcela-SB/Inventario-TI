from modulos import *
from funcoes.funcBusc import *

def buscar(self):
# ----------- LABELS E INPUTS ----------- 
    self.lbTomboBusc = Label(           # TOMBO
        self.aba_buscar, 
        text="Tombo:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbTomboBusc.place(
        relx = 0.05,
        rely = 0.05
    )
    self.inputTomboBusc = Entry(self.aba_buscar, font=50)
    self.inputTomboBusc.place(
        relx = 0.25,
        rely = 0.06,
        relwidth=0.4, 
        height=30
    )

    self.lbItemBusc = Label(           # ITEM
        self.aba_buscar, 
        text="Item:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbItemBusc.place(
        relx = 0.05,
        rely = 0.125
    )
    self.inputItemBusc = Entry(self.aba_buscar, font=50)
    self.inputItemBusc.place(
        relx = 0.25,
        rely = 0.127,
        relwidth=0.4, 
        height=30
    )

    self.lbSalaBusc = Label(           # SALA
        self.aba_buscar, 
        text="Sala:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbSalaBusc.place(
        relx = 0.05,
        rely = 0.21
    )

                                            # LISTA SUSPENSA
    numeros = [str(i) for i in range(1, 49)]  # Lista de números de 1 a 48
    self.comboboxBusc = ttk.Combobox(
        self.aba_buscar, 
        values=numeros, 
        state="readonly", 
        width=10,
    )
    self.comboboxBusc.place(
        relx=0.25, 
        rely = 0.21
    )

# ----------- BOTÕES -----------         
    self.btBuscarBusc = Button(
        self.aba_buscar,
        bg= "#347deb",
        fg= "#FFFFFF",
        text="Buscar",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtBuscar(self)
    )
    self.btBuscarBusc.place(
        relx= 0.8, 
        rely=0.04, 
        width=180, 
        height=61
    )

    self.btBuscInventario = Button(
        self.aba_buscar,
        bg= "purple",
        fg= "#FFFFFF",
        text="Inventário\nCompleto",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtBuscInventario(self)
    )
    self.btBuscInventario.place(
        relx= 0.8, 
        rely=0.15, 
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

