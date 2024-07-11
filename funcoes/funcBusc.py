from modulos import *
from conexaoBD import *

tk.botao = ""


def funcBtBuscar(self):
        messagebox.showinfo("Info", "Botão Buscar")

        # CONECTANDO O BD E INICIALIZANDO CURSOR
        conexao = conectar_bd(self)
        cursor = conexao.cursor()

        # RECEBENDO OS VALORES DOS ENTRYS
        buscTombo = self.inputTomboBusc.get()
        buscItem = self.inputItemBusc.get()
        buscSala = self.comboboxBusc.get()

        # SE TODOS OS VALORES NÃO FOREM NULL
        if buscTombo or buscItem or buscSala:
            # RESTRIÇÕES DE BUSCA
            restricoes = []
            parametros = []

            if buscTombo:
                restricoes.append("tombo = %s")
                parametros.append(buscTombo)
            
            if buscItem:
                restricoes.append("tipo = %s")
                parametros.append(buscItem)
            
            if buscSala:
                restricoes.append("salaId = %s")
                parametros.append(buscSala)

            restricoes_sql = " AND ".join(restricoes)

            try:
                query = f"SELECT tombo, tipo, ident, salaId FROM item WHERE {restricoes_sql} ORDER BY tombo ASC"
                cursor.execute(query, parametros)
                resultados = cursor.fetchall()  # Ler todos os resultados

                # Limpar Treeview
                self.lista.delete(*self.lista.get_children())

                # Exibir resultados
                for idx, resultado in enumerate(resultados, start=1):
                    tombo, tipo, ident, salaId = resultado
                    self.lista.insert("", END, iid=idx, text=idx, values=(tombo, tipo, ident, salaId))

                conexao.commit()

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
            finally:
                cursor.close()
                conexao.close()
        else:
            messagebox.showerror("Erro", "Insira ao menos uma informação para a função de busca.")


def funcBtBuscInventario(self):
    messagebox.showinfo("Info", "Botão BuscInventario")
    #self.btBuscInventario
