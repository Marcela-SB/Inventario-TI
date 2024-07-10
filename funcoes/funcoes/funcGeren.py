from modulos import *
from conexaoBD import *
from funcoes.bdBuscar import *

tk.botao = ""

def funcBtExcluir(self):
    opcaoExluir = messagebox.askyesno("Excluir item", "Confirma a exclusão do item?")

    if(opcaoExluir):
        # RECEBENDO OS VALORES DOS ENTRYS
        excTombo = str(self.inputTomboGer.get())

        # SE O VALOR NÃO FOR NULL
        if(excTombo):

            # Verificando se o item existe antes de excluir
            if verificarItem(self, excTombo):
                
                #CONECTANDO O BD E INICIALIZANDO CURSOR
                conexao = conectar_bd(self)
                cursor = conexao.cursor()
                try:
                    cursor.execute("DELETE FROM item WHERE tombo = %s", (excTombo,))
                    conexao.commit()
                    messagebox.showinfo("Sucesso", "Item excluído com sucesso!")
            
                    # APAGANDO DOS INPUTS
                    self.inputTomboGer.delete(0,END)
                    self.inputItemGer.delete(0, END)
                    self.inputDescricaoGer.delete(0,END)
                    self.valor_combobox.set("")

                except mysql.connector.Error as err:
                    messagebox.showerror("Erro", f"Erro ao excluir item: {err}")
                finally:
                    cursor.close()
                    conexao.close()

            else:
                messagebox.showwarning("Aviso", f"Item com tombo {excTombo} não encontrado. Não foi possível excluir.")

        else:
            messagebox.showerror("ERRO", "Campo de TOMBO em branco, por favor preencher!")


#///////////////////////////////////////////////////////
def funcBtAdicionar(self):
    #CONECTANDO O BD E INICIALIZANDO CURSOR
    conexao = conectar_bd(self)
    cursor = conexao.cursor()

    # RECEBENDO OS VALORES DOS ENTRYS
    adicTombo = str(self.inputTomboGer.get())
    adicItem = self.inputItemGer.get()
    adicDescricao = self.inputDescricaoGer.get()
    adicSala = self.comboboxGer.get()

    # SE TODOS OS VALORES NÃO FOREM NULL
    if(adicTombo and adicItem and adicDescricao and adicSala):
        
        # Verifica se o item já existe
        if verificarItem(self, adicTombo):
            if not messagebox.askyesno("Item existente", "Item já existe, deseja sobrescrever?"):
                return  # Cancela a adição se o usuário não deseja sobrescrever
        try:
            cursor.execute("INSERT INTO item (tombo, tipo, ident, salaId) VALUES (%s, %s, %s, %s)", (adicTombo, adicItem, adicDescricao, adicSala))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
    
            # APAGANDO DOS INPUTS
            self.inputTomboGer.delete(0,END)
            self.inputItemGer.delete(0, END)
            self.inputDescricaoGer.delete(0,END)
            self.valor_combobox.set("")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao adicionar item: {err}")
        finally:
            cursor.close()
            conexao.close()

    else:
        messagebox.showerror("ERRO", "Campos em branco, por favor preencher todos!")


#///////////////////////////////////////////////////////
def funcBtSalvarInventario(self):
    messagebox.showinfo("Info", "Botão SalvarInventario")
    #self.btSalvarInventario

def funcBtCompInventarios(self):
    messagebox.showinfo("Info", "Botão CompInventarios")
    #self.btCompInventarios
    


'''tk.botao = "AD"
                self.after(1000, show_info)
def show_info():
    if(tk.botao=="AD"):
        messagebox.showinfo("Adicionado", "Item adicionado ao Inventário com sucesso!")
    elif(tk.botao=="EX"):
        messagebox.showinfo("Excluido", "Item excluido do Inventário com sucesso!")'''