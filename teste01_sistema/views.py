import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)

print(mydb)

mycursor = mydb.cursor()


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
"""
mycursor.execute("SELECT * FROM itens WHERE tipo ='PC'")
result = mycursor.fetchall()
for c in result:
    print(c)
"""