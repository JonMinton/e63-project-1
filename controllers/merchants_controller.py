from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all() # NEW
    print(merchants)
    return render_template("/merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/<id>")
def merchant_info(id):
    merchant = merchant_repository.select(id)
    print(f"{merchant.name} has id {merchant.id}")
    merchant_tags = tag_repository.select_by_merchant(id)
    return render_template(
        "/merchants/merchant_info.html", 
        merchant = merchant,
        merchant_tags = merchant_tags
    )

@merchants_blueprint.route("/merchants/new", methods = ['POST'])
def new_merchant():
    return render_template("/merchants/new.html")

@merchants_blueprint.route("/merchants", methods = ['POST'])
def submit_new_merchant():
    name = request.form['name']
    num_sales = request.form['num_sales']
    revenue = request.form['revenue']
    merchant = Merchant(name, num_sales, revenue)
    merchant_repository.save(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/delete")
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("/merchants/edit.html", merchant = merchant)
    
@merchants_blueprint.route("/merchants/edit", methods = ['POST'])
def save_edit_merchant():
    id = request.form['merc_id']
    name = request.form['name']
    num_sales = request.form['num_sales']
    revenue = request.form['revenue']
    merchant = merchant_repository.select(id)
    merchant.name = name
    merchant.num_sales = num_sales
    merchant.revenue = revenue
    merchant_repository.update(merchant)
    return redirect("/merchants")

