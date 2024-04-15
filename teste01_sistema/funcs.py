import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)

print(mydb)

mycursor = mydb.cursor()

# funções 

# ok
def mostrar_salas():
    mycursor.execute("SELECT salaId, descricao, predio FROM salas")
    list = mycursor.fetchall()

    for c in list:
        print(f"{c[0]:<3} {c[1]:<15} {c[2]:<10}")

# ok
def inserir_item():
    item = []
    tombo = str(input("Insira o tombo do item: "))
    item.append(tombo)
    tipo = str(input("Qual item será adicionado: "))
    item.append(tipo)
    ident = str(input("Insira a descrição do item: "))
    item.append(ident)
    print("Selecione a sala que o item está: ")
    mostrar_salas()
    sala = str(input())
    item.append(sala)


    query = "INSERT INTO item (tombo, tipo, ident, idSala) VALUES (%s, %s, %s, %s)"
    val = tuple(item)
    mycursor.execute(query, val)
    mydb.commit()

# ok 
def buscar_item(tombo):
    item = []
    item.append(tombo)
    query = "SELECT i.tipo, i.salaId, s.predio FROM item as i, salas as s WHERE i.tombo = %s and i.salaId = s.salaId"
    val = tuple(item)
    mycursor.execute(query, val)
    list = mycursor.fetchall()
    for c in list:
        print(f"{c[0]:<10}{"  sala: "}{c[1]:<3}{" predio: "}{c[2]:<10}")


def tranferir_item():
    item = []
    #busca por tombo
    #buscar_item()

#mostrar_salas() # ok 
#inserir_item() # ok
#buscar_item(tombo) # ok
