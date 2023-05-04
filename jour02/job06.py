import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laplateforme.06!",
    database = "laplateforme"
)

# Créer un objet "curseur"
curseur = db.cursor()

# Exécuter la requête SQL pour calculer la somme des capacités des salles
curseur.execute("SELECT SUM(capacite) FROM salles")

# Récupérer le résultat
resultat = curseur.fetchone()

# Extraire la somme des capacités des salles du résultat
somme_capacites = resultat[0]

# Afficher le résultat dans la console
print(f"La somme des capacités des salles est de {somme_capacites}.")

# Fermer le curseur et la connexion
curseur.close()
db.close()
