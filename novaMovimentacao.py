from modulos import *
from funcoes.funcNovaMov import *
from config import nameUser

def criarNovaMovimentacao(self):
    global nameUser
    # RECEBENDO VALOR
    item = []
    item = info(self)

    # VERIFICAR EXISTÊNCIA DE TOMBO PARA ABRIR A JANELA
    if item is None:
        messagebox.showerror("Erro", "Item não encontrado.")
        return
    
    if(abrirJanelinha(self, item[0])):

        self.janelinha = Toplevel()
        self.janelinha.title("Nova Movimentação")
        self.janelinha.configure(bg= "#29273A")
        self.janelinha.geometry("500x400") # Largura x Altura
        self.janelinha.resizable(False, False)          #RESPONSIVIDADE
        self.janelinha.focus_force()
        self.janelinha.grab_set()

        self.novaMov = Frame(
            self.janelinha,
            bg= "#D9D9D9"
        )
        self.novaMov.place(
            relx= 0.05,
            rely= 0.05,
            relwidth= 0.9,
            relheight= 0.9
        )

    # ----------- BOTÕES ----------- 
        self.btCriarNovaMov = Button(
            self.novaMov,
            bg= "#2EC27B",
            fg= "#FFFFFF",
            text="Criar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command= lambda: funcBtCriarNovaMov(self)
        )
        self.btCriarNovaMov.place(
            relx= 0.6, 
            rely=0.815, 
            width=100, 
            height=45
        )
        
        self.btCancelarMov = Button(
            self.novaMov,
            bg= "#C22E2E",
            fg= "#FFFFFF",
            text="Cancelar",
            font=("Inter Regular", 24 * -1),
            relief="flat", 
            border=2,
            command= lambda: funcBtCancelarMov(self)

        )
        self.btCancelarMov.place(
            relx= 0.2, 
            rely=0.815, 
            width=100, 
            height=45
        )


    # ----------- LABELS E INPUTS ----------- 
        self.MovTombo = Label(
            self.novaMov,
            text="Tombo:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.MovTombo.place(
            relx= 0.125,
            rely= 0.075
        )
        self.inputTomboNovMov = Label(
            self.novaMov,
            text= item[0],
            bg= "#D9D9D9",
            font=("Ivy 15"), 
            fg= "blue"
            )
        self.inputTomboNovMov.place(
            relx=0.5,
            rely = 0.075
        )

        
        self.lbOrigem = Label(
            self.novaMov,
            text="Origem:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.lbOrigem.place(
            relx= 0.125,
            rely= 0.25
        )
        self.inputOrigemNovMov = Label(
            self.novaMov,
            text= item[1],
            bg= "#D9D9D9",
            font=("Ivy 15"), 
            fg= "blue"
            )
        self.inputOrigemNovMov.place(
            relx=0.5,
            rely = 0.25
        )


        self.lbDestino = Label(
            self.novaMov,
            text="Destino:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.lbDestino.place(
            relx= 0.125,
            rely= 0.45
        )
        valorSalas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'M', 'R', 'Q','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36A', '36B', '38A', '38B', '38C', '38D', '39', '40A', '40B', '40C', '45']
        self.selDestino = ttk.Combobox(
            self.novaMov, 
            values=valorSalas, 
            state="readonly", 
            width=10,
            font=50
        )
        self.selDestino.place(
            relx=0.5, 
            rely = 0.45
        )


        self.MovRespons = Label(
            self.novaMov,
            text="Responsável:",
            bg= "#D9D9D9",
            font=("Ivy 15 bold"), 
            fg= "black"   
        )
        self.MovRespons.place(
            relx= 0.125,
            rely= 0.65
        )        
        
        
        print(config.nameUser)
        self.ResponsavelNovMov = Label(
            self.novaMov,
            text= config.nameUser,
            bg= "#D9D9D9",
            font=("Ivy 15"), 
            fg= "blue"
            )
        self.ResponsavelNovMov.place(
            relx=0.5,
            rely = 0.65
        )