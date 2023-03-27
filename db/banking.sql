-- Build this after building the models, their attributes and methods
-- and testing them

DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS accounts CASCADE;
DROP TABLE IF EXISTS banks;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS customers_accounts CASCADE;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    num_sales INT,
    revenue FLOAT
);

INSERT INTO 
    merchants (name, num_sales, revenue) 
    VALUES ('Woolwireworths', 14, 120.0);

INSERT INTO 
    merchants (name, num_sales, revenue)
    VALUES ('Griff''s', 120, 1503.50);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    budget FLOAT DEFAULT 0.0
);

INSERT INTO 
    customers (first_name, last_name)
    VALUES ('Jon', 'Minton');

INSERT INTO 
    customers (first_name, last_name)
    VALUES ('Mon', 'Jinton');


CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    balance FLOAT DEFAULT 0.0
); 

INSERT INTO 
    accounts (balance)
    VALUES (500.30);

INSERT INTO 
    accounts (balance)
    VALUES (204.00);

CREATE TABLE customers_accounts (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    account_id INT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE
);

INSERT INTO 
    customers_accounts (customer_id, account_id)
    VALUES (2, 1);

INSERT INTO 
    customers_accounts (customer_id, account_id)
    VALUES (1, 2);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    merchant_id INT NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    amount FLOAT,
    timestamp TIMESTAMP
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    merchant_id INT NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    timestamp INT
);

INSERT INTO 
    tags (name, merchant_id, timestamp)
    VALUES ('Bric-a-brac', 1, 42);


