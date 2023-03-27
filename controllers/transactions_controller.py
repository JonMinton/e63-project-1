from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.transaction import Transaction
from models.account import Account
from models.customer import Customer

import repositories.transaction_repository as transaction_repository
import repositories.account_repository as account_repository
import repositories.customer_repository as customer_repository


transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all() # NEW
    return render_template("transactions/index.html", transactions = transactions)

@transactions_blueprint.route("/transactions/<id>")
def transactions_by_account(id):
    transactions = transaction_repository.select_by_account(id) # NEW
    return render_template(
        "transactions/index.html", 
        transactions = transactions,
        account_id = id
    )
