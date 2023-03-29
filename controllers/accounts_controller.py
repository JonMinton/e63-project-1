from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.account import Account
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

accounts_blueprint = Blueprint("accounts", __name__)

@accounts_blueprint.route("/accounts")
def accounts():
    accounts = account_repository.select_all() # NEW
    return render_template("accounts/index.html", accounts = accounts)

@accounts_blueprint.route("/accounts/<id>")
def account_info(id):
    account = account_repository.select(id)
    customer = account_repository.get_customer_with_account(id)
    transactions = transaction_repository.select_by_account(id)
    print(f"This account has {len(transactions)} transactions")
    merchants = merchant_repository.select_all()
    return render_template("accounts/account_info.html", 
        account = account,
        customer = customer,
        merchants = merchants,
        transactions = transactions
    )

@accounts_blueprint.route("/accounts/<id>/buy", methods = ['POST'])
def buy_from_merchant(id):
    merchant_id = request.form['merchant_id']
    price = request.form['price']
    print(f"customer id is {id}")
    print(f"merchant id is {merchant_id}")
    print(f"the price is {price}")
    account_repository.buy_from_merchant(id, merchant_id, price)

    account = account_repository.select(id)
    customer = account_repository.get_customer_with_account(id)
    merchants = merchant_repository.select_all()
    return render_template("accounts/account_info.html", 
        account = account,
        customer = customer,
        merchants = merchants
    )   

@accounts_blueprint.route("/accounts/<id>/deposit", methods = ['POST'])
def deposit_into_account(id):
    deposit_amount = request.form['deposit_amount']
    account = account_repository.select(id)
    account.balance += float(deposit_amount)
    account_repository.update(account)
    return redirect(f"/accounts/{id}")

@accounts_blueprint.route("/accounts/<id>/withdrawal", methods = ['POST'])
def withdrawal_into_account(id):
    withdrawal_amount = request.form['withdrawal_amount']
    account = account_repository.select(id)
    if account.balance >= float(withdrawal_amount):
        account.balance -= float(withdrawal_amount)
        account_repository.update(account)

    return redirect(f"/accounts/{id}")


@accounts_blueprint.route("/accounts/<id>/transactions")
def list_transactions_from_account(id):
    transactions = transaction_repository.select_by_account(id)
    return render_template(
        "accounts/account_transactions.html",
        transactions = transactions
    )

# /accounts/{{ account.id }}/buy"
# @accounts_blueprint.route("/accounts/new", methods = ['POST'])
# def new_account():
#     return render_template("accounts/new.html")

# @accounts_blueprint.route("/accounts", methods = ['POST'])
# def submit_new_account():
#     balance = request.form['balance']
#     account = Account(balance)
#     account_repository.save(account)
#     return redirect("/accounts")




# # # DELETE
# # # DELETE '/visits/<id>'
# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_task(id):
#     visit_repository.delete(id)
#     return redirect('/visits')