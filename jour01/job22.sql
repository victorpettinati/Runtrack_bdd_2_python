SELECT nom, prenom, age, email from etudiants where age = (select min(age) from etudiants);
    
+--------+--------+------+-------------------------------+
| nom    | prenom | age  | email                         |
+--------+--------+------+-------------------------------+
| Barnes | Binkie |   16 | binkie.barnes@laplateforme.io |
+--------+--------+------+-------------------------------+