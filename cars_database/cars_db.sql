SELECT * FROM cars WHERE year BETWEEN 2000 AND 2008;

SELECT * FROM cars WHERE color IN ("Violet", "Pink", "Fuscia");

SELECT * FROM cars WHERE color LIKE "Violet";

SELECT * FROM cars WHERE model LIKE "X%";

SELECT * FROM cars WHERE model LIKE "%a";

SELECT * FROM cars WHERE model LIKE "__";

SELECT * FROM cars WHERE model LIKE "X_";

SELECT * FROM cars WHERE make LIKE "__n%";

SELECT * FROM cars WHERE color IS NULL;

SELECT * FROM cars WHERE color IS NOT NULL;

INSERT INTO cars (make, model, year, price)
    VALUES ("Tesla", "Model Y", 2022, 55555);

SELECT * FROM cars WHERE make="Ford" AND year > 2000;

SELECT * FROM cars WHERE year > 2010 ORDER BY make, year;

SELECT * FROM cars WHERE color NOT IN ("Violet", "Pink", "Fuscia", "Puce", "Red");

SELECT * FROM cars
    WHERE (make = "Ford" OR make = "Volvo")
    AND price BETWEEN 20000 AND 60000;

-- Case sensitive
SELECT * FROM cars
    WHERE make = "FORD" COLLATE NOCASE;

SELECT make || ", " || model  as car, year, color FROM cars;

-- suskaiciuotas amzius
SELECT make, model, 2023-year as age FROM cars ORDER BY age;

-- PVM
SELECT make, model, year, price, ROUND(price / 1.21, 2) as price_ex_vat FROM cars;

SELECT min(year), max(year), avg(year) FROM cars;

SELECT min(price), max(price), avg(price) FROM cars;

SELECT make, model, min(price) FROM cars WHERE make = "Volvo";

SELECT make, model, min(price) FROM cars GROUP BY make;

SELECT make, model, min(price) as cheapest, count(make) as units FROM cars
    WHERE year > 1990
    GROUP BY make
    HAVING units > 1
    ORDER BY cheapest;

SELECT SUM(price) as sum FROM cars;