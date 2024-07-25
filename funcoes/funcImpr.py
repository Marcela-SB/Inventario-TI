from modulos import *
from funcoes.bdBuscar import *
from conexaoBD import *
# MODULOS IMPRESSÃO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

from tkinter.filedialog import asksaveasfilename

tk.botao = ""

def cliqueDuploImpr(self):
    self.inputTomboImpr.delete(0,END)
    self.conferindo.selection()
    for n in self.conferindo.selection():   
        colunas = self.conferindo.item(n, 'values')
        self.inputTomboImpr.insert(END, colunas[0])

def buscaImpressao(self):
    tb = self.inputTomboImpr.get()
    if tb != "":
        numtb = int(tb)

        if numtb > 10000:
            conexao = conectar_bd(self)
            cursor = conexao.cursor()

            try:
                cursor.execute(f"SELECT tombo, tipo, descricao, salaId, obs FROM item WHERE tombo LIKE '{numtb}%'")
                resultados = cursor.fetchall()  # Ler todos os resultados

                # Limpar Treeview
                self.conferindo.delete(*self.conferindo.get_children())

                # Exibir resultados
                for idx, resultado in enumerate(resultados, start=1):
                    tombo, tipo, descricao, salaId, obs = resultado
                    if(obs=="" or obs==None):
                        obs = "-"
                    self.conferindo.insert("", tk.END, iid=idx, text=idx, values=(tombo, tipo, descricao, salaId, obs))

                conexao.commit()

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
            finally:
                cursor.close()
                conexao.close()
        else:
            # Limpar Treeview
            self.conferindo.delete(*self.conferindo.get_children())


#///////////////////////////////////
def printRelatorio(self, caminho_arquivo):
            webbrowser.open(caminho_arquivo)


def funcBtImprQRCode(self):
    messagebox.showinfo("Info", "Botão ImprQRCode")
    #self.btImprQRCode


def funcBtImprCodigoBarras(self):
    messagebox.showinfo("Info", "Botão ImprCodigoBarras")
    #self.btImprCodigoBarras


def funcBtImprMov(self):
    messagebox.showinfo("Info", "Botão ImprMov")
    #self.btImprMov
    tbImpr = str(self.inputTomboImpr.get())
    existe = verificarItem(self, tbImpr)
    
    if existe:
        def gerarRelatorioMov(self):
            try:
                # Nome padrão para o arquivo
                nome_padrao_arquivo = f"Detalhamento_de_Item_{tbImpr}.pdf"

                # Obter o local para salvar o arquivo
                caminho_arquivo = asksaveasfilename(
                    defaultextension=".pdf", 
                    filetypes=[("PDF files", "*.pdf")],
                    title="Salvar relatório como",
                    initialfile=nome_padrao_arquivo
                )
                if not caminho_arquivo:
                    #messagebox.showwarning("Operação Cancelada", "Salvamento do relatório cancelado.")
                    return False
                
                # Conectar ao banco de dados
                conexao2 = conectar_bd(self)
                cursor2 = conexao2.cursor()

                # Consultar detalhes do item
                cursor2.execute("""SELECT salaOrigem, salaDestino, data, hora, responsavel FROM movimentacao WHERE tombo = %s
                ORDER BY data ASC, hora ASC""", (tbImpr,))
                item = cursor2.fetchone()  # Consumir o resultado da consulta
                if not item:
                    messagebox.showerror("Erro", "Item não encontrado.")
                    return False

                # Gerar o relatório em PDF
                self.r = canvas.Canvas(caminho_arquivo)

                self.r.setFont("Helvetica-Bold", 24)
                self.r.drawString(200, 780, f"Relatório de Item")
                
                self.r.setFont("Helvetica", 16)
                self.r.drawString(100, 730, f"Tombo: {item[0]}")


                # Salvar e fechar o PDF
                self.r.showPage()
                self.r.save()
                printRelatorio(self, caminho_arquivo)
                messagebox.showinfo("Relatório Gerado", "Relatório gerado com sucesso.")

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")
                return False
            
            finally:
                cursor2.close()   # Fechar o cursor2 após usar
                conexao2.close()  # Fechar a conexão após usar

        # Chamar a função para gerar o relatório
        gerarRelatorioMov(self)

def funcBtImprDetal(self):
    tbImpr = str(self.inputTomboImpr.get())
    existe = verificarItem(self, tbImpr)
    
    if existe:
        def gerarRelatorio(self):
            try:
                # Nome padrão para o arquivo
                nome_padrao_arquivo = f"Detalhamento_de_Item_{tbImpr}.pdf"

                # Obter o local para salvar o arquivo
                caminho_arquivo = asksaveasfilename(
                    defaultextension=".pdf", 
                    filetypes=[("PDF files", "*.pdf")],
                    title="Salvar relatório como",
                    initialfile=nome_padrao_arquivo
                )
                if not caminho_arquivo:
                    #messagebox.showwarning("Operação Cancelada", "Salvamento do relatório cancelado.")
                    return False
                
                # Conectar ao banco de dados
                conexao2 = conectar_bd(self)
                cursor2 = conexao2.cursor()

                # Consultar detalhes do item
                cursor2.execute("SELECT tombo, tipo, descricao, salaId, obs FROM item WHERE tombo = %s", (tbImpr,))
                item = cursor2.fetchone()  # Consumir o resultado da consulta
                if not item:
                    messagebox.showerror("Erro", "Item não encontrado.")
                    return False

                # Gerar o relatório em PDF
                self.r = canvas.Canvas(caminho_arquivo)

                self.r.setFont("Helvetica-Bold", 24)
                self.r.drawString(200, 780, f"Relatório de Item")
                
                self.r.setFont("Helvetica", 16)
                self.r.drawString(100, 730, f"Tombo: {item[0]}")
                self.r.drawString(100, 710, f"Tipo: {item[1]}")
                self.r.drawString(100, 690, f"Descrição: {item[2]}")
                
                # Buscar detalhes da sala com base no 'salaId'
                cursor2.execute("SELECT funcao, predio FROM salas WHERE salaId = %s", (item[3],))
                sala = cursor2.fetchone()  # Consumir o resultado da consulta
                if sala:
                    self.r.drawString(100, 670, f"Sala: {item[3]}")
                    self.r.drawString(150, 650, f"- Função: {sala[0]}")
                    self.r.drawString(150, 630, f"- Prédio: {sala[1]}")
                    self.r.drawString(100, 610, f"OBS: {item[4]}")
                else:
                    self.r.drawString(100, 670, f"Sala não encontrada para salaId: {item[3]}")
                    self.r.drawString(100, 650, f"OBS: {item[4]}")

                # Salvar e fechar o PDF
                self.r.showPage()
                self.r.save()
                printRelatorio(self, caminho_arquivo)
                messagebox.showinfo("Relatório Gerado", "Relatório gerado com sucesso.")

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")
                return False
            
            finally:
                cursor2.close()   # Fechar o cursor2 após usar
                conexao2.close()  # Fechar a conexão após usar

        # Chamar a função para gerar o relatório
        gerarRelatorio(self)


    

def funcBtImprInventario(self):
    messagebox.showinfo("Info", "Botão ImprInventario")
    #self.btImprInventario