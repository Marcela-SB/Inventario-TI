from modulos import *
from conexaoBD import *

tk.botao = ""


def funcBtBuscar(self):
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
            restricoes.append("tombo LIKE %s")
            parametros.append(f"{buscTombo}%")
        
        if buscItem:
            restricoes.append("tipo LIKE %s")
            parametros.append(f"{buscItem}%")
        
        if buscSala:
            restricoes.append("salaId = %s")
            parametros.append(buscSala)

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
                tombo, tipo, descricao, salaId, obs = resultado
                if(obs == ""):
                    obs = "-"
                self.lista.insert("", END, iid=idx, text=idx, values=(tombo, tipo, descricao, salaId, obs))

            conexao.commit()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror("ERRO", "Campos em branco, por favor preencher!")


def funcBtBuscInventario(self):
    # CONECTANDO O BD E INICIALIZANDO CURSOR
    conexao = conectar_bd(self)
    cursor = conexao.cursor()
    try:
        cursor.execute(f"SELECT tombo, tipo, descricao, salaId FROM item ORDER BY tombo ASC")
        resultados = cursor.fetchall()  # Ler todos os resultados

        # Limpar Treeview
        self.lista.delete(*self.lista.get_children())

        # Exibir resultados
        for idx, resultado in enumerate(resultados, start=1):
            tombo, tipo, descricao, salaId = resultado
            self.lista.insert("", END, iid=idx, text=idx, values=(tombo, tipo, descricao, salaId))

        conexao.commit()

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao buscar item: {err}")
    finally:
        cursor.close()
        conexao.close()

    # APAGANDO DOS INPUTS
        self.inputTomboBusc.delete(0,END)
        self.inputItemBusc.delete(0,END)
        self.comboboxBusc.set("")