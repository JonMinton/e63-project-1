from db.run_sql import run_sql

from models.customer import Customer
from models.account import Account
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository

def save(account):
    sql = "INSERT INTO accounts (balance) VALUES (%s) RETURNING *"
    values = [account.balance]
    results = run_sql(sql, values)
    id = results[0]['id']
    account.id = id

def delete(id):
    sql = "DELETE FROM accounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    accounts = []

    sql = "SELECT * FROM accounts"
    results = run_sql(sql)

    if results:
        for row in results:
            account = Account(row['balance'], row['id'] )
            accounts.append(account)

        return accounts


def select(id):
    account = []
    sql = "SELECT * FROM accounts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        account = Account(
            result['balance'], result['id'] 
            )
    else:
        return None
    
    return account

def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)


def get_customer_with_account(id):
    sql = """
        SELECT customer_id FROM customers_accounts
        WHERE account_id = %s
    """
    values = [id]
    result = run_sql(sql, values)
    customer_id = result[0]['customer_id']
    sql = """
        SELECT * FROM customers
        WHERE id = %s
    """
    values = [customer_id]
    result = run_sql(sql, values)
    result = result[0]
    customer = Customer(result['first_name'], result['last_name'], result['budget'], result['id'])

    return customer

def buy_from_merchant(id, merchant_id, price):
    sql = """
        SELECT * FROM accounts 
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)
    result = result[0]
    account = Account(result['balance'], result['id'])

    if account.balance >= price:
        sql = """
            SELECT * FROM merchants 
            WHERE id = %s
        """
        values = [merchant_id]
        result = run_sql(sql, values)
        result = result[0]

        merchant = Merchant(result['name'], result['num_sales'], result['revenue'], result['id'])
        account.balance -= price
        merchant.num_sales += 1
        merchant.revenue += price

        transaction = Transaction(account, merchant, price)
        output = transaction_repository.save(transaction)
        transaction.id = output.id

    # check if account is sufficient
    # reduce amount in account
    # increase amount in merchant
    # increment number of merchant sales
    # add transaction record

# def update(author):
#     sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [author.first_name, author.last_name, author.id]
#     run_sql(sql, values)
