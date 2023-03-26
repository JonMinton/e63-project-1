from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.account import Account
import repositories.account_repository as account_repository

accounts_blueprint = Blueprint("accounts", __name__)

@accounts_blueprint.route("/accounts")
def accounts():
    accounts = account_repository.select_all() # NEW
    return render_template("accounts/index.html", accounts = accounts)

# @accounts_blueprint.route("/accounts/<id>")
# def account_info(id):
#     account = account_repository.select(id)
#     return render_template("accounts/account_info.html", account = account)

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