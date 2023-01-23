CREATE TABLE status (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE order_ (
    id INTEGER PRIMARY KEY NOT NULL,
    customer_id INTEGER NOT NULL,
    date_ VARCHAR(20) NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (id),
    FOREIGN KEY (status_id) REFERENCES status (id)
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(40) NOT NULL,
    price DECIMAL NOT NULL
);

CREATE TABLE product_order (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES order_ (id),
    FOREIGN KEY (product_id) REFERENCES product (id)
);

INSERT INTO customer (f_name, l_name, email)
    VALUES ("Jonas", "Jonaitis", "jonas@jonaitis.com"),
    ("Ona", "Onaityte", "ona@onaityte.com"),
    ("Petras", "Petrauskas", "petras@petrauskas.com"),
    ("Birute", "Birutyte", "birute@birutyte.com");

INSERT INTO status (name)
    VALUES ("Patvirtintas"), ("Vykdomas"), ("Įvykdytas"), ("Atšauktas");

INSERT INTO product (name, price)
    VALUES ("Citrinžolių eterinis aliejus", 5.49),
    ("Arbatmedžio eterinis aliejus", 4.79),
    ("Pipirmėčių eterinis aliejus", 5.99),
    ("Čiobrelių eterinis aliejus", 13.99),
    ("Rožių žiedų vanduo", 5.99),
    ("Jojobos aliejus", 9.99),
    ("Saldžiųjų migdolų aliejus", 3.59),
    ("Mėginėlių rinkinys", 5.99);

INSERT INTO order_ (customer_id, date_, status_id)
    VALUES (1, "2023-01-15", 3),
    (4, "2023-01-16", 4),
    (4, "2023-01-17", 3),
    (3, "2023-01-18", 2),
    (2, "2023-01-19", 1),
    (3, "2023-01-19", 1),
    (1, "2023-01-19", 4);

INSERT INTO product_order (order_id, product_id, quantity)
    VALUES (1, 1, 1), (1, 4, 1), (1, 7, 2),
    (2, 5, 2), (2, 8, 1),
    (3, 1, 1), (3, 3, 1), (3, 4, 1), (3, 5, 3),
    (4, 8, 1),
    (5, 6, 3), (5, 7, 1),
    (6, 2, 2), (6, 4, 1), (6, 8, 1),
    (7, 4, 1), (7, 5, 2), (7, 7, 1);

SELECT order_.id, date_ as date, customer.f_name || " " || customer.l_name as customer, sum(product.price * product_order.quantity) as price FROM order_
    JOIN customer ON customer_id = customer.id
    JOIN product_order ON order_id = order_.id
    JOIN product ON product_id = product.id
    JOIN status ON status_id = status.id
    WHERE NOT status.id = 4
    GROUP BY order_.id;

SELECT order_.id, product.name, product_order.quantity, product.price, product.price * product_order.quantity as total_price FROM order_
    JOIN product_order ON order_id = order_.id
    JOIN product ON product_id = product.id
    JOIN status ON status_id = status.id
    WHERE NOT status_id = 4;

SELECT product.name, sum(product_order.quantity) as quantity, product.price, sum(product.price * product_order.quantity) as total_price FROM product
    JOIN product_order ON product_id = product.id
    JOIN order_ ON order_id = order_.id
    JOIN status ON status_id = status.id
    WHERE NOT status_id = 4
    GROUP BY product.name;