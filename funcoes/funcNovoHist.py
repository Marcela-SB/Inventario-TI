from modulos import *
from conexaoBD import *

tk.botao = ""

def funcBtNovoHist(self):
    opcaoNovoHist = messagebox.askyesno("Novo histórico", "Confirma a criação da nova Entrada no Histórico?\nVerifique as informações com cuidado.")

    #RECEBENDO DADOS
    nvhTombo = self.inputTomboNovHist.get()
    nvhOrigem = self.selOrigem.get()
    nvhDestino = self.selDestino.get()
    nvhResp = self.selResponsavel.get()

    if(nvhTombo and nvhOrigem and nvhDestino and nvhResp):
        ''try:
        
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()
            
            '''cursor.execute("INSERT INTO item (tombo, tipo, ident, salaId) VALUES (%s, %s, %s, %s)", (adicTombo, adicItem, adicDescricao, adicSala))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
    
            # APAGANDO DOS INPUTS
            self.inputTomboGer.delete(0,END)
            self.inputItemGer.delete(0, END)
            self.inputDescricaoGer.delete(0,END)
            self.valor_combobox.set("")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao adicionar item: {err}")'''''
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("ERRO", "Campos em branco, por favor preencher todos!")

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
