CREATE TABLE coder (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(200) UNIQUE,
    age INTEGER CHECK (age > 17 AND age < 75),
    experience INTEGER CHECK (experience < 40)
);

INSERT INTO coder (first_name, last_name, email, age, experience)
    VALUES ("Kestutis", "Januskevicius", "kestas@midonow.fi", 39, 25);

SELECT * FROM coder;

ALTER TABLE coder ADD COLUMN project_id INTEGER;
ALTER TABLE coder ADD COLUMN team_id INTEGER;

DROP TABLE coder;