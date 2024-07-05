from modulos import *
from tkinter import messagebox

tk.botao = ""

def funcBtNovoHist(self):
    opcaoNovoHist = messagebox.askyesno("Novo histórico", "Confirma a criação da nova Entrada no Histórico?\nVerifique as informações com cuidado.")
    print(opcaoNovoHist)
    if(opcaoNovoHist):
        tk.botao = "NV"
        self.after(1000, show_info)

def show_info():
    messagebox.showinfo("Adicionado", "Nova Entrda no Histórico adicionada com sucesso!")



def funcBtCancelarHist(self):
    opcaoCancelarHist = messagebox.askyesno("Sair de Novo Histórico", "Deseja mesmo cancelar a nova Entrada em Histórico?")
    if(opcaoCancelarHist):
        self.janelinha.destroy()