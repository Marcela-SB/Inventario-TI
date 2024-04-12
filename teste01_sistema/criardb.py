import mysql.connector

#Cria o database dentro do mySQL é executado se não houver a existência do database Inventario *não editar o arquivo


mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE inventario")

mycursor.execute("CREATE DATABASE inventario")

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)
mycursor = mydb.cursor()

# criando tabela salas
mycursor.execute("CREATE TABLE SALAS (salaId CHAR(3) PRIMARY KEY, descricao BINARY(0), predio BINARY(0))")

# criando tabela itens
mycursor.execute("CREATE TABLE ITENS (tombo CHAR(10) PRIMARY KEY, tipo VARCHAR(20), ident VARCHAR(50), idSala CHAR(3), FOREIGN KEY (idSala) REFERENCES SALAS(salaId))")

# criando tabela movimentação
mycursor.execute("CREATE TABLE MOVIMENTACAO (id INT AUTO_INCREMENT PRIMARY KEY, ItemID CHAR(10), FOREIGN KEY(ItemID) REFERENCES ITENS(tombo), salaOrigemID CHAR(3), FOREIGN KEY(salaOrigemID) REFERENCES SALAS(salaId), salaDestinoID CHAR(3), FOREIGN KEY(salaDestinoID) REFERENCES SALAS(salaId), data DATE)")


