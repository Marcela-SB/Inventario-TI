from modulos import *
from conexaoBD import *
from datetime import datetime

tk.botao = ""

def funcBtNovoHist(self):
    #RECEBENDO DADOS
    nvhTombo = self.inputTomboNovHist.get()
    nvhOrigem = self.selOrigem.get()
    nvhDestino = self.selDestino.get()
    nvhResp = self.selResponsavel.get()

    if(nvhTombo and nvhOrigem and nvhDestino and nvhResp):
        try:
        
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()
            
            cursor.execute("INSERT INTO movimentacao (itemID, salaOrigem, salaDestino, data, responsavel) VALUES (%s, %s, %s, %s, %s)", (nvhTombo, nvhOrigem, nvhDestino, datetime.today().date(), nvhResp))
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