import mysql.connector

class Employee:

    def __init__(self, db):
        self.db = db

    def _connect(self):
        return mysql.connector.connect(
            host=self.db['host'],
            user=self.db['user'],
            password=self.db['password'],
            database=self.db['database']
        )

    def create_employee(self, nom, prenom, salaire, id_service):
        db = self._connect()
        curseur = db.cursor()

        curseur.execute("""
        INSERT INTO employes (nom, prenom, salaire, id_service)
        VALUES (%s, %s, %s, %s)
        """, (nom, prenom, salaire, id_service))

        db.commit()
        curseur.close()
        db.close()

    def read_employee(self, employee_id):
        db = self._connect()
        curseur = db.cursor()

        curseur.execute("SELECT * FROM employes WHERE id = %s", (employee_id,))
        resultat = curseur.fetchone()

        curseur.close()
        db.close()

        return resultat

    def update_employee(self, employee_id, nom, prenom, salaire, id_service):
        db = self._connect()
        curseur = db.cursor()

        curseur.execute("""
        UPDATE employes
        SET nom = %s, prenom = %s, salaire = %s, id_service = %s
        WHERE id = %s
        """, (nom, prenom, salaire, id_service, employee_id))

        db.commit()
        curseur.close()
        db.close()

    def delete_employee(self, employee_id):
        db = self._connect()
        curseur = db.cursor()

        curseur.execute("DELETE FROM employes WHERE id = %s", (employee_id,))

        db.commit()
        curseur.close()
        db.close()

# Exemple d'utilisation
db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Laplateforme.06!',
    'database': 'entreprise'
}

employee = Employee(db)

# Créer un employé
# employee.create_employee('Jean-Pierre', 'Janette', 1894, 1)

# Lire un employé
print(employee.read_employee(1))

# Mettre à jour un employé
employee.update_employee(1, 'Jean-Pierre', 'Janette', 5000, 1)

# Supprimer un employé
employee.delete_employee(4)
