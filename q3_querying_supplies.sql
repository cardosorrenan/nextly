CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(64) NOT NULL,
    city VARCHAR(64) NOT NULL
);

CREATE TABLE parts (
    part_id INT PRIMARY KEY,
    part_name VARCHAR(64) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE cars (
    car_id INT PRIMARY KEY,
    car_name VARCHAR(64) NOT NULL,
    car_type VARCHAR(64) NOT NULL
);

CREATE TABLE supplies (
    supplier_id INT,
    part_id INT,
    car_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (part_id) REFERENCES parts(part_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id),
    PRIMARY KEY (supplier_id, part_id, car_id)
);


SELECT sup.supplier_name as 'SUPPLIER', part.price as 'PRICE'
FROM suppliers sup
JOIN supplies sups ON sup.supplier_id = sups.supplier_id
JOIN parts part ON sups.part_id = part.part_id
JOIN cars car ON sups.car_id = car.car_id
WHERE sup.city = 'VITORIA' AND part.part_name = 'MOTOR' AND car.car_name = 'KOMBI';