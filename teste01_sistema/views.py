import mysql.connector
from funcs import * 

tab = "\t"

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)

print(mydb)

mycursor = mydb.cursor()

# funcoes

def menu_salas():
    print("\n\t"f"{'MENU DE SALAS':^}")
    print("\t"f"{'1 - VER SALA':^}")
    print("\t"f"{'2 - EDITAR SALA':^}")
    print("\t"f"{'3 - ADICIONAR SALA':^}") 
    print("\t"f"{'9 - EXCLUIR SALA':^}\n") 
    opc = str(input("\t"f"{'SELECIONE UMA OPÇÃO:':^}"))
    
    # switch py
    if opc == '1':
        #ver_sala()
        print("1")
    elif opc == '2':
        #editar_sala()
        print("2")
    elif opc == '3':
        #adicionar_sala()
        print("3")
    elif opc == '9':
        #deletar_sala()
        print("9")
        
def menu_itens():
    print("\n\t"f"{'MENU DE SALAS':^}")
    print("\t"f"{'1 - LISTAR TODOS OS ITENS':^}")
    print("\t"f"{'2 - PESQUISAR ITEM':^}")
    print("\t"f"{'3 - ADICIONAR ITEM':^}")
    print("\t"f"{'4 - EDITAR ITEM':^}")  
    print("\t"f"{'9 - EXCLUIR ITEM':^}\n") 
    opc = str(input("\t"f"{'SELECIONE UMA OPÇÃO:':^}"))
    
    # switch py
    if opc == '1':
        #listar_itens()
        print("1")
    elif opc == '2':
        #buscar_itens()
        print("2")
    elif opc == '3':
        #adicionar_item()
        print("3")
    elif opc == '4':
        #editar_item()
        print("4")
    elif opc == '9':
        #deletar_item()
        print("9")


def menu_inicial():
    print("\n\t"f"{'MENU INICIAL':^}")
    print("\t"f"{'1 - MENU DE SALAS':^}")
    print("\t"f"{'2 - MENU DE ITENS':^}")
    print("\t"f"{'3 - MENU DE MOVIMENTAÇÃO':^}\n") 
    opc = str(input("\t"f"{'SELECIONE UMA OPÇÃO:':^}"))
    
    # switch py
    if opc == '1':
        menu_salas()
        print("1")
    elif opc == '2':
        menu_itens()
        print("2")
    elif opc == '3':
        #menu_historico()
        print("3")
        
        
        
    
    





def criar_sala():
    query = "INSERT INTO salas (salaId, descricao) VALUES (%s, %s)"
    val = []
    val.append(str(input("Número da sala: ")))
    val.append(str(input("Descrição da sala: ")))
    mycursor.execute(query, val)
    mydb.commit()


'''
def excluir_sala():
    opc = 1
    while opc != 0:
        opc = int(input("Deseja excluir uma sala? (1-SIM | 0-NÃO)"))
        if opc == 1:    
            mycursor.execute("SELECT salaId FROM salas")
            result = mycursor.fetchall()
            for x in result:
                print(x)

            query = "DELETE FROM salas WHERE salaId = %s"    
            val = str(input("sala: "))
            mycursor.execute(query, val)
            mydb.commit()
'''
def verificar_sala(salaId):
    query = ("SELECT salaId FROM inventario.salas WHERE salaId = '%s'")
    val = salaId
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        return 1
    else:
        return 0

def criar_item():
    query = "INSERT INTO item (tombo, tipo, ident, salaId) VALUES (%s, %s, %s, %s)"
    itens = []
    itens.append(str(input("Indique o tombo do item: ")))
    itens.append(str(input("Indique o tipo do item: ")))
    itens.append(str(input("Descreva o item: ")))
    sala = str(input("Indique a sala que o item está: "))
    if verificar_sala(sala) == 1:
        itens.append(sala)
    elif verificar_sala == 0:
        print("A sala não existe, selecione uma opção")
        opc = input("0-Selecionar outra sala | 1-Criar sala {sala}")
        if opc == 1:
            criar_sala()
        elif opc == 0:
            sala = str(input("Indique a sala que o item está: "))
            itens.append(sala)

    
    mycursor.execute(query, itens)
    mydb.commit()

#criar_sala()
#criar_item()

menu_inicial()

"""
# excluindo tabela para ser criada novamente (já que é apenas um teste)
mycursor.execute("TRUNCATE TABLE itens")

# inserindo item no itens -> (tombo, tipo, ident)
sql = "INSERT INTO itens (tombo, tipo, ident) VALUES (%s, %s, %s)"
val = ("2019003691", "PC", "Computador de mesa - Desktop")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "item inserido , ID: ", mycursor.lastrowid)

#inserindo item 2
val = ("2019003692", "PC", "Computador de mesa - Desktop")
mycursor.execute(sql, val)
mydb.commit()

#inserindo item 3
val = ("2022004675", "CAMERA", "Câmera fotográfica - Nikon")
mycursor.execute(sql, val)
mydb.commit()

# imprimindo tudo da tabela
mycursor.execute("SELECT * FROM itens")
result = mycursor.fetchall()
for c in result:
    print(c)

# 
mycursor.execute("SELECT tombo, tipo FROM itens")
result = mycursor.fetchall()
for c in result:
    print(c)

# buscando apenas uma linha (a primeira)
mycursor.execute("SELECT * FROM itens")
result = mycursor.fetchone()
print(result)



# buscando por valor único // deu errado

mycursor.execute("SELECT * FROM itens WHERE tipo ='PC'")
result = mycursor.fetchall()
for c in result:
    print(c)
"""