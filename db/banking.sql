-- Build this after building the models, their attributes and methods
-- and testing them

DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    num_sales INT,
    revenue FLOAT
);

INSERT INTO 
    merchants (name, num_sales, revenue) 
    VALUES ('Woolwireworths', 14, 120.0);