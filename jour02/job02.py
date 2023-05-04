import mysql.connector

# Remplacez ces valeurs par vos informations d'identification
user = 'root'
password = 'Laplateforme.06!'
host = 'localhost'
database = 'laplateforme'

# Établir la connexion à la base de données
cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Définir la requête SQL pour créer la table "etage"
create_etage_table_query = '''
CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
)
'''

# Exécuter la requête SQL pour créer la table "etage"
cursor.execute(create_etage_table_query)

# Définir la requête SQL pour créer la table "salles"
create_salles_table_query = '''
CREATE TABLE salles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT,
    FOREIGN KEY (id_etage) REFERENCES etage(id)
)
'''

# Exécuter la requête SQL pour créer la table "salles"
cursor.execute(create_salles_table_query)

# Valider la transaction
cnx.commit()

# Fermer le curseur et la connexion
cursor.close()
cnx.close()