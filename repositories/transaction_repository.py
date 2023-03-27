from db.run_sql import run_sql

from models.merchant import Merchant
from models.account import Account
from models.transaction import Transaction
from models.customer import Customer

import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository


def save(transaction):
    sql = "INSERT INTO transactions (account_id, merchant_id, amount, timestamp) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.account.id, transaction.merchant.id, transaction.amount, transaction.timestamp]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    if results:
        for row in results:
            transaction = Transaction(
                account_repository.select(row['account_id']), 
                merchant_repository.select(row['merchant_id']), 
                row['amount'], row['timestamp'] 
            )
            transactions.append(transaction)

        return transactions


def select(id):
    customer = []
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'falsy' 
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

def select_by_account(account_id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE account_id = %s"
    values = [account_id]
    results = run_sql(sql, values)

    if results:
        for row in results:
            transaction = Transaction(
                account_repository.select(row['account_id']), 
                merchant_repository.select(row['merchant_id']), 
                row['amount'], 
                row['timestamp'], 
                row['id']
            )
            transactions.append(transaction)
    
    return transactions




# def update(author):
#     sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [author.first_name, author.last_name, author.id]
#     run_sql(sql, values)


