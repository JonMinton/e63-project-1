from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all() # NEW
    return render_template("customers/index.html", customers = customers)

@customers_blueprint.route("/customers/<id>")
def customer_info(id):
    customer = customer_repository.select(id)
    customer_accounts = customer_repository.get_customer_accounts(id)
    customer_accounts_sum = sum([account.balance for account in customer_accounts])
    return render_template(
        "customers/customer_info.html", 
        customer = customer, customer_accounts = customer_accounts,
        customer_accounts_sum = customer_accounts_sum
    )

@customers_blueprint.route("/customers/<id>/open_new_account", methods = ['POST'])
def open_new_account(id):
    customer_id = id
    print(f"customer_id is {customer_id}")
    deposit = request.form['deposit_amount']
    print(f"deposit is {deposit}")
    customer_repository.open_new_account(customer_id, deposit)
    return redirect("/customers")

@customers_blueprint.route("/customers/new", methods = ['POST'])
def new_customer():
    return render_template("customers/new.html")

@customers_blueprint.route("/customers", methods = ['POST'])
def submit_new_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    budget = request.form['budget']
    customer = Customer(first_name, last_name, budget)
    customer_repository.save(customer)
    return redirect("/customers")

@customers_blueprint.route("/customers/<id>/edit")
def open_customer_edit(id):
    customer_to_edit = customer_repository.select(id)
    return render_template(
        "/customers/edit.html",
        customer = customer_to_edit
    )

@customers_blueprint.route("/customers/edit", methods = ['POST'])
def make_customer_edit():
    new_first_name = request.form['first_name']
    print(f"first name: {new_first_name}")
    new_last_name = request.form['last_name']
    new_budget = request.form['budget']
    customer_id = request.form['cust_id']
    customer = customer_repository.select(customer_id)
    customer.first_name = new_first_name
    customer.last_name = new_last_name
    customer.budget = new_budget
    customer_repository.update(customer)
    return redirect("/customers")


@customers_blueprint.route("/customers/<id>/delete")
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")

