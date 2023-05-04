mysql> update etudiants set age = 20 where prenom = 'Betty';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select*from etudiants where prenom = 'Betty';
+----+-----------+--------+------+---------------------------------+
| id | nom       | prenom | age  | email                           |
+----+-----------+--------+------+---------------------------------+
|  1 | Spaghetti | Betty  |   20 | betty.Spaghetti@laplateforme.io |
+----+-----------+--------+------+---------------------------------+