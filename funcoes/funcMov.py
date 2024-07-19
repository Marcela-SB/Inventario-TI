from modulos import *
from conexaoBD import *

tk.botao = ""


def funcbtBuscarMov(self):
    # CONECTANDO O BD E INICIALIZANDO CURSOR
    conexao = conectar_bd(self)
    cursor = conexao.cursor()

    # RECEBENDO OS VALORES DOS ENTRYS
    tbMov = self.inputTomboMov.get()
    dataMov = self.inputDataMov.get()
    salaMov = self.comboboxMov.get()

    # SE TODOS OS VALORES NÃO FOREM NULL
    if tbMov or dataMov or salaMov:
        # RESTRIÇÕES DE BUSCA
        restricoes = []
        parametros = []

        if tbMov:
            restricoes.append("tombo LIKE %s")
            parametros.append(f"{tbMov}%")
        
        if dataMov:
            restricoes.append("tipo WHERE %s")
            parametros.append(f"{dataMov}")
        
        if salaMov:
            restricoes.append("salaId = %s")
            parametros.append(salaMov)

        restricoes_sql = " AND ".join(restricoes)

        try:
            query = f"""SELECT tombo, tipo, descricao, salaId, obs FROM item WHERE {restricoes_sql} 
            ORDER BY tombo ASC"""
            cursor.execute(query, parametros)
            resultados = cursor.fetchall()  # Ler todos os resultados

            # Limpar Treeview
            self.lista.delete(*self.lista.get_children())

            # Exibir resultados
            for idx, resultado in enumerate(resultados, start=1):
                tombo, item, salaOrigem, salaDestino, responsavel = resultado
                self.entradas.insert("", END, iid=idx, text=idx, values=(tombo, item, salaOrigem, salaDestino,"?? : ??", "hora", responsavel))

            conexao.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("ERRO", "Campo em branco, por favor insira TOMBO!")