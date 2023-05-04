mysql> select id, nom, prenom, age, email from etudiants where prenom like 'b%';

+----+-----------+--------+------+---------------------------------+
| id | nom       | prenom | age  | email                           |
+----+-----------+--------+------+---------------------------------+
|  1 | Spaghetti | Betty  |   23 | betty.Spaghetti@laplateforme.io |
|  4 | Barnes    | Binkie |   16 | binkie.barnes@laplateforme.io   |
+----+-----------+--------+------+---------------------------------+