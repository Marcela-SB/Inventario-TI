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


def funcBtCriarNovaMov(self):
    #RECEBENDO DADOS
    item = []
    item = info(self)
    nvmDestino = self.selDestino.get()
    nvmResp = config.nameUser

    if(nvmDestino != item[1]):
        try:
            
            # Conectar ao banco de dados
            conexao = conectar_bd(self)
            cursor = conexao.cursor()
            
            # CRIANDO NOVA MOVIMENTAÇÃO
            cursor.execute("INSERT INTO movimentacao (itemID, salaOrigem, salaDestino, data, responsavel) VALUES (%s, %s, %s, %s, %s)", (item[0], item[1], nvmDestino, datetime.now(), nvmResp))
            conexao.commit()

            #ALTERANDO SALA ATUAL NO ITEM
            cursor.execute("UPDATE item SET salaId = %s WHERE tombo = %s", (nvmDestino, item[0]))

            conexao.commit()

            messagebox.showinfo("Sucesso", "Movimentação criada com sucesso!")
            
            self.janelinha.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao criar nova movimentação: {err}")
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("Erro", f"O item já está nesta sala! ")



def funcBtCancelarMov(self):
    opcaoCancelarMov = messagebox.askyesno("Sair de Nova Movimentação", "Deseja mesmo cancelar a nova Entrada em Movimentação?")
    if(opcaoCancelarMov):
        self.janelinha.destroy()

