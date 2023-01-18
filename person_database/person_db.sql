SELECT * FROM person;

SELECT first_name, last_name FROM person;

SELECT gender FROM person;

SELECT DISTINCT gender FROM person;

SELECT * FROM person WHERE gender="Female";

SELECT * FROM person WHERE date_of_birth > date("1999-01-01");

SELECT * FROM person
    WHERE date_of_birth > "1999-01-01"
    AND date_of_birth < "2003-01-01"
    AND GENDER = "Female";

SELECT * FROM person ORDER BY gender DESC, first_name, last_name;

SELECT gender, count(gender) AS count FROM person
    WHERE date_of_birth >= "1999-01-01"
    GROUP BY gender
    HAVING count > 1;

SELECT first_name || " " || last_name AS vardas FROM person ORDER BY last_name;