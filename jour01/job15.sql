mysql> select id, nom, prenom, age, email from etudiants order by nom ASC;

+----+-----------+----------+------+---------------------------------+
| id | nom       | prenom   | age  | email                           |
+----+-----------+----------+------+---------------------------------+
|  4 | Barnes    | Binkie   |   16 | binkie.barnes@laplateforme.io   |
|  3 | Doe       | John     |   18 | john.doe@laplateforme.io        |
|  5 | Dupuis    | Gertrude |   20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |   18 | martin.dupuis@laplateforme.io   |
|  1 | Spaghetti | Betty    |   23 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |   45 | chuck.steak@laplateforme.io     |
+----+-----------+----------+------+---------------------------------+