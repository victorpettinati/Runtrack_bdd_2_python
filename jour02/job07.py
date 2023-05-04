import mysql.connector

# Configurer la connexion à MySQL (sans spécifier de base de données)
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laplateforme.06!",
    database = "entreprise"
)
# Créer un objet "curseur"
curseur = db.cursor()

#curseur.execute("CREATE DATABASE entreprise")

#print("La base de données a été créée avec succès.")

# Créer la table employes
#curseur.execute("""
#CREATE TABLE employes (
    #id INT AUTO_INCREMENT PRIMARY KEY,
    #nom VARCHAR(255),
    #prenom VARCHAR(255),
    #salaire DECIMAL(10, 2),
    #id_service INT
#)
#""")

# Créer la table services
#curseur.execute("""
#CREATE TABLE services (
    #id INT AUTO_INCREMENT PRIMARY KEY,
    #nom VARCHAR(255)
#)
#""")

# Insérer des employés dans la table employes
employes = [
    ('Dupont', 'Pierre', 3500, 1),
    ('Martin', 'Alice', 2500, 1),
    ('Bernard', 'Jean', 4500, 2),
    ('Durand', 'Sophie', 3000, 2),
]

# for employe in employes:
#     curseur.execute("""
#     INSERT INTO employes (nom, prenom, salaire, id_service)
#     VALUES (%s, %s, %s, %s)
#     """, employe)

# Insérer des services dans la table services
services = [
    ('Informatique',),
    ('Ressources Humaines',),
]

for service in services:
    curseur.execute("""
    INSERT INTO services (nom)
    VALUES (%s)
    """, service)

# Valider les modifications dans la base de données
db.commit()

# Récupérer les employés dont le salaire est supérieur à 3000 €
curseur.execute("SELECT * FROM employes WHERE salaire > 3000")
resultats = curseur.fetchall()

print("Employés avec un salaire supérieur à 3000 € :")
for resultat in resultats:
    print(resultat)

# Récupérer tous les employés et leur service respectif
curseur.execute("""
SELECT employes.id, employes.nom, employes.prenom, employes.salaire, services.nom
FROM employes
JOIN services ON employes.id_service = services.id
""")
resultats = curseur.fetchall()

print("\nEmployés et leur service respectif :")
for resultat in resultats:
    print(resultat)

# Fermer le curseur et la connexion
curseur.close()
db.close()