import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Laplateforme.06!",
    database = "entreprise"
)

curseur = db.cursor()

class Zoo:

    def __init__(self, db_config):
        self.db_config = db_config

    def _connect(self):
        return mysql.connector.connect(
            host=self.db_config['host'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            database=self.db_config['database']
        )

    def add_cage(self, superficie, capacite_max):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("""
        INSERT INTO cage (superficie, capacite_max)
        VALUES (%s, %s)
        """, (superficie, capacite_max))

        db.commit()
        cursor.close()
        db.close()

    def remove_cage(self, cage_id):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("DELETE FROM cage WHERE id = %s", (cage_id,))

        db.commit()
        cursor.close()
        db.close()

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("""
        INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
        VALUES (%s, %s, %s, %s, %s)
        """, (nom, race, id_cage, date_naissance, pays_origine))

        db.commit()
        cursor.close()
        db.close()

    def remove_animal(self, animal_id):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("DELETE FROM animal WHERE id = %s", (animal_id,))

        db.commit()
        cursor.close()
        db.close()

    def update_animal(self, animal_id, nom, race, id_cage, date_naissance, pays_origine):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("""
        UPDATE animal
        SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s
        WHERE id = %s
        """, (nom, race, id_cage, date_naissance, pays_origine, animal_id))

        db.commit()
        cursor.close()
        db.close()

    def list_animals(self):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM animal")
        resultats = cursor.fetchall()

        cursor.close()
        db.close()

        return resultats

    def list_cage_animals(self, cage_id):
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM animal WHERE id_cage = %s", (cage_id,))
        resultats = cursor.fetchall()

        cursor.close
