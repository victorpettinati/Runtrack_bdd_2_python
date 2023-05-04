import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laplateforme.06!",
    database = "laplateforme"
)
print(db)

cursor = db.cursor()

sql1 = "INSERT INTO etage (id, nom, numero, superficie) VALUES (%s, %s, %s, %s)"
val1 = ( None, "RDC", 0, 500)
sql2 = "INSERT INTO etage (id, nom, numero, superficie) VALUES (%s, %s, %s, %s)"
val2 = (None, "R+1", 1, 500)
sql3 = "INSERT INTO salles (id, nom, id_etage, capacite) VALUES (%s, %s, %s, %s)"
val3 = (None, "Lounge", 1, 100)
sql4 = "INSERT INTO salles (id, nom, id_etage, capacite) VALUES (%s, %s, %s, %s)"
val4 = (None, "Sutdio Son", 1, 5)
sql5 = "INSERT INTO salles (id, nom, id_etage, capacite) VALUES (%s, %s, %s, %s)"
val5 = (None, "Broadcasting", 2, 50)
sql6 = "INSERT INTO salles (id, nom, id_etage, capacite) VALUES (%s, %s, %s, %s)"
val6 = (None, "Bocal Peda", 2, 4)
sql7 = "INSERT INTO salles (id, nom, id_etage, capacite) VALUES (%s, %s, %s, %s)"
val7 = (None, "Corworking", 2, 80)
sql8 = "INSERT INTO salles (id, nom, id_etage, capacite) VALUES (%s, %s, %s, %s)"
val8 = (None, "Studio Video", 2, 5)

cursor.execute(sql1, val1)
cursor.execute(sql2, val2)
cursor.execute(sql3, val3)
cursor.execute(sql4, val4)
cursor.execute(sql5, val5)
cursor.execute(sql6, val6)
cursor.execute(sql7, val7)
cursor.execute(sql8, val8)

db.commit()

print(cursor.rowcount, "record inserted.")