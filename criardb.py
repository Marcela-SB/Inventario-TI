import mysql.connector

# Conecta ao MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
)

mycursor = mydb.cursor()

# mycursor.execute("DROP DATABASE inventario")
# mycursor.execute("CREATE DATABASE inventario")

# Cria o database se não existir
mycursor.execute("CREATE DATABASE IF NOT EXISTS inventario")

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
    CREATE TABLE IF NOT EXISTS salas (
        salaId CHAR(3) PRIMARY KEY,
        funcao VARCHAR(30),
        predio VARCHAR(10)
    )
""")

# Criando tabela item
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS item (
        tombo INT(12) PRIMARY KEY NOT NULL,
        tipo VARCHAR(20) NOT NULL,
        descricao VARCHAR(50) DEFAULT NULL,
        salaId CHAR(3) NOT NULL,
        FOREIGN KEY (salaId) REFERENCES salas(salaId),
        obs VARCHAR(50) DEFAULT NULL
    )
""")

# Criando tabela movimentacao
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS movimentacao (
        id INT AUTO_INCREMENT PRIMARY KEY,
        itemID INT(12),
        FOREIGN KEY (itemID) REFERENCES item(tombo),
        salaOrigemId CHAR(3),
        FOREIGN KEY (salaOrigemId) REFERENCES salas(salaId),
        salaDestino CHAR(3),
        FOREIGN KEY (salaDestino) REFERENCES salas(salaId),
        data DATE,
        hora TIME,
        responsavel VARCHAR(50)
    )
""")

# Renomear coluna 'c1' para 'c2' na tabela 'tab'
'''mycursor.execute("""
    ALTER TABLE tab 
    CHANGE COLUMN c1 c2 TipoDados(?)
""")'''

# Excluir coluna 'c1' da tabela 'tab'
'''mycursor.execute("""
    ALTER TABLE tab 
    DROP COLUMN c1
""")'''

# Alterar coluna 'c1' da tabela 'tab'
'''mycursor.execute("""ALTER TABLE tab 
MODIFY COLUMN c1 TipoDados(?);""")'''

# Fecha a conexão
mydb.close()

print("Banco de dados e tabelas criados e modificados com sucesso!")
