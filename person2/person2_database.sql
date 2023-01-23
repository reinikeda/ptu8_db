SELECT * FROM person;

SELECT * FROM car;

SELECT * FROM company;

-- WHERE

SELECT person.first_name, person.last_name, car.make, car.plate FROM person, car
    WHERE person.car_id = car.id;

SELECT last_name, name as company_name, make FROM person, company, car
    WHERE person.company_id = company.id AND person.car_id = car.id
    ORDER BY name, make;

-- JOIN

SELECT last_name, make, model FROM person
    JOIN car ON person.car_id = car.id;

SELECT last_name, plate, name FROM person
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE company_id = 5;

SELECT last_name, make, model, plate, name FROM person
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE make = "Ford"
    ORDER BY name DESC;

SELECT name, count(*) as count FROM person
    JOIN company ON company_id = company.id
    GROUP BY name
    HAVING count > 3;

SELECT plate FROM car
    JOIN person ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE company.name = "Apple";

SELECT company.id, name FROM company
    JOIN person ON person.company_id = company.id
    GROUP BY name
    HAVING count(*) <= 3
    ORDER BY name;

SELECT first_name, last_name, make, name FROM person
    JOIN car ON person.car_id = car.id
    JOIN company ON person.company_id = company.id
    WHERE person.company_id IN (
        SELECT company.id FROM company
            JOIN person ON person.company_id = company.id
            GROUP BY name
            HAVING count(*) <= 3
            ORDER BY name
    );

SELECT first_name, last_name, make, model, plate FROM person
    LEFT JOIN car ON car_id = car.id;

INSERT INTO car (make, model, plate)
    VALUES ("Dethleffs", "A1558", "BGI555");

-- SELECT first_name, last_name, make, model, plate FROM person
--     RIGHT JOIN car ON car_id = car.id;

SELECT first_name, last_name, make, model FROM car
    LEFT JOIN person ON person.car_id = car.id;