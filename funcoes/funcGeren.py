from modulos import *
from tkinter import messagebox

tk.botao = ""
 
def funcBtExcluir(self):
    opcaoExluir = messagebox.askyesno("Excluir item", "Confirma a exclusão do item?")
    print(opcaoExluir)
    if(opcaoExluir):
        self.inputTomboGer.delete(0,END)
        self.inputItemGer.delete(0, END)
        self.inputDescricaoGer.delete(0,END)
        self.valor_combobox.set("")
        tk.botao = "EX"
        self.after(500, show_info)
 
def funcBtAdicionar(self):
    opcaoAdicionar = messagebox.askyesno("Adicionar item", "Confirma a adição do item?\nVerifique as informações com cuidado.")
    print(opcaoAdicionar)
    if(opcaoAdicionar):
        self.inputTomboGer.delete(0,END)
        self.inputItemGer.delete(0, END)
        self.inputDescricaoGer.delete(0,END)
        self.valor_combobox.set("")
        tk.botao = "AD"
        self.after(1000, show_info)

def show_info():
    if(tk.botao=="AD"):
        messagebox.showinfo("Adicionado", "Item adicionado ao Inventário com sucesso!")
    elif(tk.botao=="EX"):
        messagebox.showinfo("Excluido", "Item excluido do Inventário com sucesso!")


def funcBtSalvarInventario(self):
    messagebox.showinfo("Info", "Botão SalvarInventario")
    #self.btSalvarInventario

def funcBtCompInventarios(self):
    messagebox.showinfo("Info", "Botão CompInventarios")
    #self.btCompInventarios
