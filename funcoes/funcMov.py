from modulos import *
from conexaoBD import *

tk.botao = ""

def cliqueDuploMov(self):
    print(config.bt)
    self.inputTomboMov.delete(0,END)
    self.valor_comboboxMov.set("")

    self.entradas.selection()

    for n in self.entradas.selection():   
        colunas = self.entradas.item(n, 'values')
        self.inputTomboMov.insert(END, colunas[0])
        self.radio_var.set(False)
        self.btSelCalendMov.config(text='não considerar', bg="#ff9999")

def funcbtBuscarMov(self):
    # CONECTANDO O BD E INICIALIZANDO CURSOR
    conexao = conectar_bd(self)
    cursor = conexao.cursor()

    # RECEBENDO OS VALORES DOS ENTRYS
    tbMov = self.inputTomboMov.get()
    getData = self.radio_var.get()  # vou usar data?
    dataMov = self.cal.get_date()  # se usar a data
    salaMov = self.comboboxMov.get()

    # SE TODOS OS VALORES NÃO FOREM NULL
    if tbMov or getData or salaMov:
        # RESTRIÇÕES DE BUSCA
        restricoes = []
        parametros = []

        if tbMov:
            restricoes.append("i.tombo LIKE %s")
            parametros.append(f"{tbMov}%")

        if getData:
            restricoes.append("m.data = %s")
            parametros.append(dataMov)

        if salaMov:
            restricoes.append("m.salaOrigem = %s OR m.salaDestino = %s")
            parametros.extend([salaMov, salaMov])

        restricoes_sql = " AND ".join(restricoes)

        try:            
            query = f"""SELECT m.itemID, i.tipo, m.salaOrigem, m.salaDestino, m.data, m.responsavel 
            FROM movimentacao m
            JOIN item i ON m.itemID = i.tombo 
            WHERE {restricoes_sql} 
            ORDER BY m.data ASC"""
            cursor.execute(query, parametros)
            resultados = cursor.fetchall()  # Ler todos os resultados

            # Limpar Treeview
            self.entradas.delete(*self.entradas.get_children())


            if not resultados:
                #self.entradas.insert("", END, iid=0, text="", values=("Resultado não encontrado", "", "", "", "", ""))
                messagebox.showwarning("Não existe", "Item buscado não existe ou não possui movimentações.")
            else:
            # Exibir resultados
                for idx, resultado in enumerate(resultados, start=1):
                    tombo, tipo, salaOrigem, salaDestino, data, responsavel = resultado
                    self.entradas.insert("", END, iid=idx, text=idx, values=(tombo, tipo, salaOrigem, salaDestino, data, "hh:mm", responsavel))


            conexao.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("ERRO", "Campos em branco, por favor preencher!")
