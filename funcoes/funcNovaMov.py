from modulos import *
from conexaoBD import *
from datetime import datetime

tk.botao = ""

"""def getDados(self):
    getTombo = self.inputTomboNovHist.get()
    if(getTombo):
        try:
        
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()
            querry = "select salaId from inventario.item where tombo = %s"
            val = tuple(getTombo)
            cursor.execute(querry, val)
            ret = cursor.fetchall()
            return ret
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar nova movimentação: {err}")
        finally:
            cursor.close()
            conexao.close()"""

def funcBtNovoHist(self):
    #RECEBENDO DADOS
    nvmTombo = self.inputTomboNovHist.get()
    nvmOrigem = self.selOrigem.get()
    nvmDestino = self.selDestino.get()
    nvmResp = self.selResponsavel.get()

    if(nvmTombo and nvmOrigem and nvmDestino and nvmResp):
        try:
        
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()
            
            cursor.execute("INSERT INTO movimentacao (itemID, salaOrigem, salaDestino, data, responsavel) VALUES (%s, %s, %s, %s, %s)", (nvmTombo, nvmOrigem, nvmDestino, datetime.now(), nvmResp))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Movimentação criada com sucesso!")
            
            self.janelinha.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar nova movimentação: {err}")
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("ERRO", "Campos em branco, por favor preencher todos!")



def funcBtCancelarHist(self):
    opcaoCancelarHist = messagebox.askyesno("Sair de Novo Histórico", "Deseja mesmo cancelar a nova Entrada em Histórico?")
    if(opcaoCancelarHist):
        self.janelinha.destroy()
