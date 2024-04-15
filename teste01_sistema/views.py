import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)

print(mydb)

mycursor = mydb.cursor()

# funcoes

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

criar_sala()
criar_item()

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