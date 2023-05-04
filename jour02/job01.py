import mysql.connector

# Remplacez ces valeurs par vos informations d'identification
user = 'root'
password = 'Laplateforme.06!'
host = 'localhost'
database = 'Laplateforme'

# Établir la connexion à la base de données
cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Exécuter la requête pour récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiants"  # Adaptez cette requête en fonction de la structure de votre table
cursor.execute(query)

# Parcourir et afficher les résultats de la requête
print("Liste des étudiants :")
for row in cursor:
    print(row)

# Fermer le curseur et la connexion
cursor.close()
cnx.close()