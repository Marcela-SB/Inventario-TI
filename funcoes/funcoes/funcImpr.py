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

tk.botao = ""

def funcBtImprQRCode(self):
    messagebox.showinfo("Info", "Botão ImprQRCode")
    #self.btImprQRCode


def funcBtImprCodigoBarras(self):
    messagebox.showinfo("Info", "Botão ImprCodigoBarras")
    #self.btImprCodigoBarras


def funcBtImprHist(self):
    messagebox.showinfo("Info", "Botão ImprHist")
    #self.btImprHist
    

def funcBtImprDetal(self):
    tbImpr = str(self.inputTomboImpr.get())
    existe = verificarItem(self, tbImpr)
    
    if existe:
        def printRelatorio(self):
            webbrowser.open("Detalhes_de_Item.pdf")

        def gerarRelatorio(self):
            try:
                # Conectar ao banco de dados
                conexao = conectar_bd(self)
                cursor2 = conexao.cursor()

                # Consultar detalhes do item
                cursor2.execute("SELECT tombo, tipo, ident, salaId FROM item WHERE tombo = %s", (tbImpr,))
                item = cursor2.fetchone()  # Consumir o resultado da consulta
                if not item:
                    messagebox.showerror("Erro", "Item não encontrado.")
                    return False

                # Gerar o relatório em PDF
                self.r = canvas.Canvas("Detalhes_de_Item.pdf")
                self.r.drawString(100, 750, f"Detalhes do Item - Tombo: {item[0]}")
                self.r.drawString(100, 730, f"Tipo: {item[1]}")
                self.r.drawString(100, 710, f"Identificação: {item[2]}")
                
                # Buscar detalhes da sala com base no 'salaId'
                cursor2.execute("SELECT tipo, descricao, predio FROM salas WHERE salaId = %s", (item[3],))
                sala = cursor2.fetchone()  # Consumir o resultado da consulta
                if sala:
                    self.r.drawString(100, 690, f"Sala: {item[3]} - Tipo: {sala[0]} - Descrição: {sala[1]} - Prédio: {sala[2]}")
                else:
                    self.r.drawString(100, 690, f"Sala não encontrada para salaId: {item[3]}")

                # Salvar e fechar o PDF
                self.r.showPage()
                self.r.save()
                printRelatorio(self)
                messagebox.showinfo("Relatório Gerado", "Relatório gerado com sucesso.")

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")
                return False
            
            finally:
                cursor2.close()   # Fechar o cursor2 após usar
                conexao.close()  # Fechar a conexão após usar

        # Chamar a função para gerar o relatório
        gerarRelatorio(self)


    

def funcBtImprInventario(self):
    messagebox.showinfo("Info", "Botão ImprInventario")
    #self.btImprInventario