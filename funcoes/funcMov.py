from modulos import *
from conexaoBD import *

tk.botao = ""


def funcbtBuscarMov(self):
    # CONECTANDO O BD E INICIALIZANDO CURSOR
    conexao = conectar_bd(self)
    cursor = conexao.cursor()

    # RECEBENDO OS VALORES DOS ENTRYS
    tbMov = self.inputTomboMov.get()

    # SE TODOS OS VALORES NÃO FOREM NULL
    if tbMov:
        try:
            cursor.execute(f"""
                SELECT m.data, m.salaOrigem, m.salaDestino, m.responsavel, i.descricao 
                FROM movimentacao m
                JOIN item i ON m.itemID = i.tombo 
                WHERE i.tombo = {tbMov}
                ORDER BY m.id ASC
            """)
            resultados = cursor.fetchall()  # Ler todos os resultados

            # Limpar Treeview
            self.entradas.delete(*self.entradas.get_children())

            # Exibir resultados
            for idx, resultado in enumerate(resultados, start=1):
                data, salaOrigem, salaDestino, responsavel, item = resultado
                self.entradas.insert("", END, iid=idx, text=idx, values=(tbMov, item, salaOrigem, salaDestino, data, "?? : ??", responsavel))

            conexao.commit()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("ERRO", "Campo em branco, por favor insira TOMBO!")