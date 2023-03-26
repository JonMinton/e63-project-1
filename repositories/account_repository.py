from db.run_sql import run_sql

from models.account import Account

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
        account = account(
            result['balance'], result['id'] 
            )
    else:
        return None
    
    return account

def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)





# def update(author):
#     sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [author.first_name, author.last_name, author.id]
#     run_sql(sql, values)
