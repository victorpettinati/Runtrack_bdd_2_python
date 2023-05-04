mysql> select id, nom, prenom, age, email from etudiants where age between 18 and 25;

+----+-----------+----------+------+---------------------------------+
| id | nom       | prenom   | age  | email                           |
+----+-----------+----------+------+---------------------------------+
|  1 | Spaghetti | Betty    |   23 | betty.Spaghetti@laplateforme.io |
|  3 | Doe       | John     |   18 | john.doe@laplateforme.io        |
|  5 | Dupuis    | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |   18 | martin.dupuis@laplateforme.io   |