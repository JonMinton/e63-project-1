from db.run_sql import run_sql

from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, num_sales, revenue) VALUES (%s, %s, %s) RETURNING *"
    values = [merchant.name, merchant.num_sales, merchant.revenue]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    if results:
        for row in results:
            merchant = Merchant(row['name'], row['num_sales'], row['revenue'], row['id'] )
            merchants.append(merchant)

        return merchants


def select(id):
    merchant = []
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        merchant = Merchant(
            result['name'], result['num_sales'], 
            result['revenue'], result['id'] 
            )
    else:
        return None
    
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)





# def update(author):
#     sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [author.first_name, author.last_name, author.id]
#     run_sql(sql, values)
