from db.run_sql import run_sql

from models.customer import Customer
from models.account import Account

def save(customer):
    sql = "INSERT INTO customers (first_name, last_name, budget) VALUES (%s, %s, %s) RETURNING *"
    values = [customer.first_name, customer.last_name, customer.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    customers = []

    sql = "SELECT * FROM customers"
    results = run_sql(sql)

    if results:
        for row in results:
            customer = Customer(row['first_name'], row['last_name'], row['budget'], row['id'] )
            customers.append(customer)

        return customers


def select(id):
    customer = []
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        customer = Customer(
            result['first_name'], result['last_name'], 
            result['budget'], result['id'] 
            )
    else:
        return None
    
    return customer

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)


def update(customer):
    sql = "UPDATE customers SET (first_name, last_name, budget) = (%s, %s, %s) WHERE id = %s"
    values = [customer.first_name, customer.last_name, customer.budget, customer.id]
    run_sql(sql, values)


def get_customer_accounts(customer_id):
    sql = """
    SELECT * FROM accounts WHERE id IN (
        SELECT account_id 
        FROM customers_accounts WHERE customer_id = %s
    );    
    """
    values = [customer_id]
    result = run_sql(sql, values)
    accounts = []
    if result:
        for row in result:
            account = Account(row['balance'], row['id'])
            accounts.append(account)
        
    return accounts

def open_new_account(customer_id, deposit):
    sql = """
    INSERT INTO accounts (balance)
        VALUES (%s)
        RETURNING *
    """
    values = [deposit]
    result = run_sql(sql, values)
    new_account_id = result[0]['id']
    print(f"new_account_id is {new_account_id}")
    sql = """
    INSERT INTO customers_accounts (customer_id, account_id)
        VALUES (%s, %s)
        RETURNING *
    """
    values = [customer_id, new_account_id]
    run_sql(sql, values)
