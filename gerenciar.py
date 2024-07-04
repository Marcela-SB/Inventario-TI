from modulos import *

def gerenciar(self):
    
    self.separator1 = Frame(         # SEPARADOR 1
        self.aba_gerenciar, 
        bg="#9B9B9B", 
        height=2, 
        bd=0
     )
    self.separator1.place(
        relx=0.01, 
        rely=0.45, 
        relwidth=0.98) 
    
    self.separator2 = Frame(         # SEPARADOR 2
        self.aba_gerenciar, 
        bg="#9B9B9B", 
        height=2, 
        bd=0
     )
    self.separator2.place(
        relx=0.01, 
        rely=0.75, 
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
        rely=0.1, 
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
        rely=0.3, 
        width=180, 
        height=61
    )

    self.btSalvarInventario = Button(
        self.aba_gerenciar,
        bg= "black",
        fg= "#FFFFFF",
        text="Salvar\nInventário Atual",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: print("Salvar Inventário Atual")
    )
    self.btSalvarInventario.place(
        relx= 0.8, 
        rely=0.62, 
        width=180, 
        height=70
    )

    self.btCompInventarios = Button(
        self.aba_gerenciar,
        bg= "black",
        fg= "#FFFFFF",
        text="Comparar\nInventários",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: print("Comparar Inventários")
    )
    self.btCompInventarios.place(
        relx= 0.8, 
        rely=0.82, 
        width=180, 
        height=70
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
        text="Descrição:", 
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



# ----------- COMPARAÇÃO INVENTÁRIOS ----------- 
    self.lbComp = Label(
        self.aba_gerenciar, 
        text="Comparar                                                    com", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbComp.place(
        relx = 0.05,
        rely = 0.85
    )
    
                                              # LISTA SUSPENSA
    backups = [str(i) for i in range(1, 6)]  # Lista de números de 1 a 5
    self.combobox = ttk.Combobox(
        self.aba_gerenciar, 
        values=backups, 
        font=50,
        state="readonly", 
        width=15
    )
    self.combobox.place(
        relx=0.2, 
        rely = 0.85
    )
    style = ttk.Style()
    style.configure('TCombobox', padding=(10, 5, 10, 5), arrowsize=15)


                                                      # LISTA SUSPENSA
    backups = [str(i) for i in range(1, 6)]  # Lista de números de 1 a 5
    self.combobox = ttk.Combobox(
        self.aba_gerenciar, 
        values=backups, 
        font=50,
        state="readonly", 
        width=15
    )
    self.combobox.place(
        relx=0.5, 
        rely = 0.85
    )
    style = ttk.Style()
    style.configure('TCombobox', padding=(10, 5, 10, 5), arrowsize=15)
