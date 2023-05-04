import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laplateforme.06!",
    database = "laplateforme"
)

# Créer un objet "curseur"
curseur = db.cursor()

# Exécuter la requête SQL pour récupérer les noms et capacités des salles
curseur.execute("SELECT nom, capacite FROM salles")

# Récupérer tous les résultats
resultats = curseur.fetchall()

# Afficher les résultats dans la console
for resultat in resultats:
    nom, capacite = resultat
    print(f"Nom: {nom}, Capacité: {capacite}")

# Fermer le curseur et la connexion
curseur.close()
db.close()
