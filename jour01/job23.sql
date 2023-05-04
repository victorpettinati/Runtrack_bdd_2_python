mysql> select nom, prenom, age, email from etudiants where age = (select max(age) from etudiants);

+-------+--------+------+-----------------------------+
| nom   | prenom | age  | email                       |
+-------+--------+------+-----------------------------+
| Steak | Chuck  |   45 | chuck.steak@laplateforme.io |
+-------+--------+------+-----------------------------+