# importando o SQLite
import sqlite3 as lite

# crando a conexão com o banco de dados
con = lite.connect('dados.db')

# Criando uma tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Inventario(tombo TEXT PRIMARY KEY, nome TEXT, tipo TEXT, local_atual TEXT, local_anterior TEXT, descricao TEXT, data_de_movimentacao DATE)")

    
