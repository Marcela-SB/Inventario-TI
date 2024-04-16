import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="inventario"
)

print(mydb)

mycursor = mydb.cursor()

for c in range(1, 34, 1):
    query = "INSERT INTO salas (salaId) VALUES (%s)"
    list = []
    list.append(c)
    app = tuple(list)
    mycursor.execute(query, app)
    mydb.commit()