from modulos import *
from conexaoBD import *
from funcoes.bdBuscar import *
from datetime import datetime

tk.botao = ""

def abrirJanelinha(self, gtb):
    if(verificarItem(self, gtb)):
        return True
    else:
        return False


def info(self):
    getTombo = str(self.inputTomboMov.get())
    if(getTombo):
        try:
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()
            
            cursor.execute("SELECT tombo, salaId FROM item WHERE tombo = %s", (getTombo,))
            item = cursor.fetchone()


        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar dados de item: {err}")
            item = None
        finally:
            cursor.close()
            conexao.close()
        #getUser = 
        return item
    
    else:
        messagebox.showwarning("Atenção!", "Campo de TOMBO em branco! Por favor preencher.")
        return False


"""def getDados(self):
    getTombo = self.inputTomboNovMov.get()
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

def funcBtCriarNovaMov(self):
    #RECEBENDO DADOS
    nvmTombo = self.inputTomboNovMov.get()
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



def funcBtCancelarMov(self):
    opcaoCancelarMov = messagebox.askyesno("Sair de Nova Movimentação", "Deseja mesmo cancelar a nova Entrada em Movimentação?")
    if(opcaoCancelarMov):
        self.janelinha.destroy()

