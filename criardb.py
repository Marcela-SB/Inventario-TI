import mysql.connector

# Conecta ao MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
)

mycursor = mydb.cursor()

# Cria o database se não existir

# Conecta ao banco de dados inventario
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)
mycursor = mydb.cursor()

# Criando tabela salas
mycursor.execute("""
    CREATE TABLE salas (
        salaId CHAR(3) PRIMARY KEY,
        funcao VARCHAR(30),
        predio VARCHAR(10)
    )
""")

# Criando tabela item
mycursor.execute("""
    CREATE TABLE item (
        tombo CHAR(10) PRIMARY KEY,
        tipo VARCHAR(20),
        descricao VARCHAR(50),
        salaId CHAR(3),
        FOREIGN KEY (salaId) REFERENCES salas(salaId)
    )
""")

# Criando tabela movimentação
mycursor.execute("""
    CREATE TABLE movimentacao (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ItemID CHAR(10),
        FOREIGN KEY (ItemID) REFERENCES item(tombo),
        salaOrigemID CHAR(3),
        FOREIGN KEY (salaOrigemID) REFERENCES salas(salaId),
        salaDestinoID CHAR(3),
        FOREIGN KEY (salaDestinoID) REFERENCES salas(salaId),
        data DATE,
        responsavel VARCHAR(50)
    )
""")

# Fecha a conexão
mydb.close()

print("Banco de dados e tabelas criados e modificados com sucesso!")
