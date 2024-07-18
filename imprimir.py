from modulos import *    
from funcoes.funcImpr import *

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
        text="Selecione o que deseja imprimir do item acima: (necessita do TOMBO)", 
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

    self.lbTomboImpr = Label(           # TOMBO
        self.aba_imprimir, 
        text="Tombo:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbTomboImpr.place(
        relx = 0.05,
        rely = 0.05
    )
    self.inputTomboImpr = Entry(self.aba_imprimir, font=50)
    self.inputTomboImpr.place(
        relx = 0.25,
        rely = 0.05,
        relwidth=0.4, 
        height=30
    )

# ----------- BOTÕES -----------
    self.btImprQRCode = Button(
        self.aba_imprimir,
        bg= "#cc6d2d",
        fg= "#FFFFFF",
        text="QR Code",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtImprQRCode(self)
    )
    self.btImprQRCode.place(
        relx= 0.15, 
        rely=0.8, 
        width=180, 
        height=61
    )

    self.btImprCodigoBarras = Button(
        self.aba_imprimir,
        bg= "#cc6d2d",
        fg= "#FFFFFF",
        text="Cód. de Barras",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtImprCodigoBarras(self)
    )
    self.btImprCodigoBarras.place(
        relx= 0.4, 
        rely=0.8, 
        width=180, 
        height=61
    )

    self.btImprMov = Button(
        self.aba_imprimir,
        bg= "#cc6d2d",
        fg= "#FFFFFF",
        text="Movimentação",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtImprMov(self)
    )
    self.btImprMov.place(
        relx= 0.15, 
        rely=0.65, 
        width=180, 
        height=61
    )

    self.btImprDetal = Button(
        self.aba_imprimir,
        bg= "#cc6d2d",
        fg= "#FFFFFF",
        text="Detalhes Item",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtImprDetal(self)
    )
    self.btImprDetal.place(
        relx= 0.4, 
        rely=0.65, 
        width=180, 
        height=61
    )

    self.btImprInventario = Button(
        self.aba_imprimir,
        bg= "purple",
        fg= "#FFFFFF",
        text="Imprimir\nInventário\nCompleto",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtImprInventario(self)
    )
    self.btImprInventario.place(
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
    self.conferindo.heading("#5", text="OBS")

    self.conferindo.column("#0", width=0, stretch=tk.NO)

    self.conferindo.place(
        relx= 0.0, 
        rely=0.0, 
        relwidth=1, 
        relheight=1
    )