from modulos import *
from conexaoBD import *

tk.botao = ""

def cliqueDuploBusc(self):
    global bt
    alterarBt("edit")
    print(config.bt)
    self.inputTomboGer.delete(0,END)
    self.inputItemGer.delete(0, END)
    self.inputDescricaoGer.delete(0,END)
    self.valor_combobox.set("")
    self.inputObsGer.delete(0,END)

    self.lista.selection()

    for n in self.lista.selection():   
        colunas = self.lista.item(n, 'values')
        self.inputTomboGer.insert(END, colunas[0])
        self.inputItemGer.insert(END, colunas[1])
        self.inputDescricaoGer.insert(END, colunas[2])
        self.valor_combobox.set(colunas[3])
        self.inputObsGer.insert(END, colunas[4])

    
    self.after(250, self.notebook.select(self.aba_gerenciar))


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

            
            if not resultados:
                #self.lista.insert("", END, iid=0, text="", values=("", "", "Resultado não encontrado", "", ""))
                messagebox.showwarning("Não existe", "Item buscado não existe.")
            else:
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
        cursor.execute(f"SELECT tombo, tipo, descricao, salaId, obs FROM item ORDER BY tombo ASC")
        resultados = cursor.fetchall()  # Ler todos os resultados

        # Limpar Treeview
        self.lista.delete(*self.lista.get_children())

        # Exibir resultados

        for idx, resultado in enumerate(resultados, start=1):
            tombo, tipo, descricao, salaId, obs = resultado
            if(obs == "" or None):
                obs = "-"
            self.lista.insert("", END, iid=idx, text=idx, values=(tombo, tipo, descricao, salaId, obs))


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