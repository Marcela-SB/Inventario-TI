from modulos import *
from funcoes.funcGeren import *
from config import bt

Vbt = config.bt

def gerenciar(self):
    print("GEN" + Vbt)
    global bt
    
    self.separator1 = Frame(         # SEPARADOR 1
        self.aba_gerenciar, 
        bg="#9B9B9B", 
        height=2, 
        bd=0
     )
    self.separator1.place(
        relx=0.01, 
        rely=0.55, 
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
    if (Vbt == "add"):
        print(Vbt)
        self.btAdicionar = Button(
            self.aba_gerenciar,
            bg= "#2EC27B",
            fg= "#FFFFFF",
            text="Adicionar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: funcBtAdicionar(self)
        )
        self.btAdicionar.place(
            relx= 0.8, 
            rely=0.1, 
            width=180, 
            height=61
        )
    if(Vbt == "edit"):
        print(Vbt)
        self.btEditar = Button(
            self.aba_gerenciar,
            bg= "blue",
            fg= "#FFFFFF",
            text="Editar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command=lambda: funcBtEditar(self)
        )
        self.btEditar.place(
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
        command= lambda: funcBtExcluir(self)
    )
    self.btExcluir.place(
        relx= 0.8, 
        rely=0.3, 
        width=180, 
        height=61
    )
    
    '''balaoExcluir = tix.Balloon(self.aba_gerenciar)
    balaoExcluir.bind_widget(self.btExcluir, balloonmsg = "Necessário apenas o TOMBO")'''

    self.btSalvarInventario = Button(
        self.aba_gerenciar,
        bg= "purple",
        fg= "#FFFFFF",
        text="Salvar\nInventário Atual",
        font=("Inter Regular", 24 * -1),
        relief="flat", 
        border=2,
        command=lambda: funcBtSalvarInventario(self)
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
        command=lambda: funcBtCompInventarios(self)
    )
    self.btCompInventarios.place(
        relx= 0.8, 
        rely=0.82, 
        width=180, 
        height=70
    )


# ----------- LABELS E INPUTS ----------- 

    self.lbTomboGer = Label(           # TOMBO
        self.aba_gerenciar, 
        text="Tombo:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbTomboGer.place(
        relx = 0.05,
        rely = 0.05
    )
    comandoValidacao = self.register(validarEntrada)
    self.inputTomboGer = Entry(
        self.aba_gerenciar, 
        font=50, 
        validate="key", 
        validatecommand=(comandoValidacao, '%d', '%P')
    )
    self.inputTomboGer.place(
        relx = 0.175,
        rely = 0.05,
        relwidth=0.4, 
        height=30
    )

    self.lbItemGer = Label(           # ITEM
        self.aba_gerenciar, 
        text="Item:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbItemGer.place(
        relx = 0.05,
        rely = 0.125
    )
    self.inputItemGer = Entry(self.aba_gerenciar, font=50)
    self.inputItemGer.place(
        relx = 0.175,
        rely = 0.127,
        relwidth=0.4, 
        height=30
    )

    self.lbDescricaoGer = Label(           # DESCRIÇÃO
        self.aba_gerenciar, 
        text="Descrição:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbDescricaoGer.place(
        relx = 0.05,
        rely = 0.21
    )
    self.inputDescricaoGer = Entry(self.aba_gerenciar, font=50)
    self.inputDescricaoGer.place(
        relx = 0.175,
        rely = 0.21,
        relwidth=0.4, 
        height=30
    )

    

    self.lbSalaGer = Label(           # SALA
        self.aba_gerenciar, 
        text="Sala:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbSalaGer.place(
        relx = 0.05,
        rely = 0.3
    )
    

                                    # LISTA SUSPENSA
    valorSalas = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'M', 'R', 'Q','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36A', '36B', '38A', '38B', '38C', '38D', '39', '40A', '40B', '40C', '45'] 
     
    self.valor_comboboxGer = tk.StringVar()
    self.comboboxGer = ttk.Combobox(
        self.aba_gerenciar, 
        textvariable=self.valor_comboboxGer,
        values=valorSalas, 
        font=50,
        state="readonly", 
        width=10
    )
    self.comboboxGer.place(
        relx=0.175, 
        rely = 0.31
    )
    style = ttk.Style()
    style.configure('TCombobox', padding=(10, 5, 10, 5), arrowsize=15)

    self.lbObsGer = Label(           # OBS
        self.aba_gerenciar, 
        text="OBS:", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbObsGer.place(
        relx = 0.05,
        rely = 0.4
    )
    self.inputObsGer = Entry(self.aba_gerenciar, font=50)
    self.inputObsGer.place(
        relx = 0.175,
        rely = 0.41,
        relwidth=0.4, 
        height=30
    )





# ----------- COMPARAÇÃO INVENTÁRIOS ----------- 
    self.lbCompGer = Label(
        self.aba_gerenciar, 
        text="Comparar                                                    com", 
        bg="#D9D9D9",
        font=("Ivy 15 bold"), 
        fg= "black"                     
    )
    self.lbCompGer.place(
        relx = 0.05,
        rely = 0.85
    )
    
                                              # LISTA SUSPENSA
    backups = [str(i) for i in range(1, 6)]  # Lista de números de 1 a 5
    self.comboboxBack1 = ttk.Combobox(
        self.aba_gerenciar, 
        values=backups, 
        font=50,
        state="readonly", 
        width=15
    )
    self.comboboxBack1.place(
        relx=0.2, 
        rely = 0.85
    )
    style = ttk.Style()
    style.configure('TCombobox', padding=(10, 5, 10, 5), arrowsize=15)


                                                      # LISTA SUSPENSA
    backups = [str(i) for i in range(1, 6)]  # Lista de números de 1 a 5
    self.comboboxBack2 = ttk.Combobox(
        self.aba_gerenciar, 
        values=backups, 
        font=50,
        state="readonly", 
        width=15
    )
    self.comboboxBack2.place(
        relx=0.5, 
        rely = 0.85
    )
    style = ttk.Style()
    style.configure('TCombobox', padding=(10, 5, 10, 5), arrowsize=15)