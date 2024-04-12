import sqlite3 as lite
from datetime import datetime

# criando conexão
con = lite.connect('dados.db')

# Inserindo inventário
def inserir_item(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Inventario (tombo, nome, tipo, local_atual, local_anterior, descricao, data_de_movimentacao) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query, i)

def excluir_item(i):
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Inventario WHERE tombo=?", (i,))
        

def atualizar_item(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET tombo=?, nome=?, descricao=?"

def troca_de_sala(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET sala_anterior = sala_atual, sala_atual=?"
        cur.execute(query, i)

def listar_itens():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for c in rows:
            lista_itens.append(c)
    return lista_itens

def ver_item_tombo(tombo):
    listar_itens = []
    with con:   
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE tombo=?", (tombo,))
        rows = cur.fetchall()
        for c in rows:
            listar_itens.append(c)
    return listar_itens

def ver_item_tipo(tipo):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE tipo=?", (tipo,))
        rows = cur.fetchall()
        for c in rows:
            lista_itens.append(c)
    return lista_itens


def func1(item1):

    inserir_item(item1)
    print("itens inseridos")
    print("\nitens do iventario")
    itens = listar_itens()
    for c in itens:
        print(c)
    print("\nitem com base no tombo")
    itensT = ver_item_tombo(item1[0])
    for c in itensT:
            print(c)

    print("\nitem com base no tipo")

    itensTp = ver_item_tipo(item1[2])
    for c in itensTp:
        print(c)

item1 = ['123456', 'PC', 'Mesa', 'sala 34', 'sala 35', 'computador dell de 8gbRAM', '25/03/2024']


item2 = ['12345', 'PC', 'Mesa', 'sala 38', 'sala 34', 'computador dell de 16gbRAM', '26/03/2024']
print(item1[0]+"\n\n")
func1(item1)
func1(item2)
#excluir_item('123456')
listaA = listar_itens()
for c in listaA:
    print(c)
