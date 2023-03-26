-- Build this after building the models, their attributes and methods
-- and testing them

DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS banks;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS transactions;
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

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    merchant_id INT NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    timestamp INT
);

INSERT INTO 
    tags (name, merchant_id, timestamp)
    VALUES ('Bric-a-brac', 1, 42);



CREATE TABLE banks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    account_id INT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    tag_id INT NOT NULL REFERENCES tags(id) ON DELETE CASCADE
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    account_id INT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE
);




CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    balance FLOAT DEFAULT 0.0,
    transaction_id INT NOT NULL REFERENCES transactions(id) ON DELETE CASCADE,
    tag_id INT NOT NULL REFERENCES tags(id)
); 

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    merchant_id INT NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    amount FLOAT,
    timestamp INT
);