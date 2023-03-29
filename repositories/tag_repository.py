from db.run_sql import run_sql

from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository


def save(tag):
    sql = "INSERT INTO tags (name, merchant_id) VALUES (%s, %s) RETURNING *"
    values = [tag.name, tag.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    if results:
        for row in results:
            tag = Tag(
                row['name'],
                merchant_repository.select(row['merchant_id']),
                row['id']
            )
            tags.append(tag)

    return tags


def select(id):
    tag = []
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'falsy' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        tag = Tag(
            result['name'],
            merchant_repository.select(result['merchant_id']),
            result['id']
        )
    else:
        return None
    
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def update(tag):
    sql = "UPDATE tags SET (name, merchant_id) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.merchant.id, tag.id]
    run_sql(sql, values)