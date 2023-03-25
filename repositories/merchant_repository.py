from db.run_sql import run_sql


from models.merchant import Merchant

# Going to try making a method which works on initialisation
def init_save_get_id(name, num_sales, revenue):
    sql = "INSERT INTO merchants (name, num_sales, revenue) VALUES (%s, %s, %s) RETURNING *"
    values = [name, num_sales, revenue]
    results = run_sql(sql, values)
    id = results[0]['id']
    return id

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

# def save(author):
#     sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
#     values = [author.first_name, author.last_name]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     author.id = id






# def select(id):
#     author = []
#     sql = "SELECT * FROM authors WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
#     # Could alternativly have..
#     # if len(results) > 0 
#     if results:
#         result = results[0]
#         author = Author(result['first_name'], result['last_name'], result['id'] )
#     else:
#         return None
    
#     return author


# def delete_all():
#     sql = "DELETE FROM authors"
#     run_sql(sql)





# def update(author):
#     sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [author.first_name, author.last_name, author.id]
#     run_sql(sql, values)
