import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laplateforme.06!",
    database = "laplateforme"
)

# Créer un objet "curseur"
curseur = db.cursor()

# Exécuter la requête SQL pour calculer la superficie totale des étages
curseur.execute("SELECT SUM(superficie) FROM etage")

# Récupérer le résultat
resultat = curseur.fetchone()

# Extraire la superficie totale (X) du résultat
superficie_totale = resultat[0]

# Afficher le résultat dans la console
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermer le curseur et la connexion
curseur.close()
db.close()
