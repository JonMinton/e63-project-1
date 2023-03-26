from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all() # NEW
    return render_template("merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/<id>")
def merchant_info(id):
    merchant = merchant_repository.select(id)
    print(f"{merchant.name} has id {merchant.id}")
    return render_template("merchants/merchant_info.html", merchant = merchant)

@merchants_blueprint.route("/merchants/new", methods = ['POST'])
def new_merchant():
    return render_template("merchants/new.html")

@merchants_blueprint.route("/merchants", methods = ['POST'])
def submit_new_merchant():
    name = request.form['name']
    print(f"name submitted by form is {name}")
    merchant = Merchant(name)
    print(f"The merchant object made has name {merchant.name}, with {merchant.num_sales} initial sales")
    merchant_repository.save(merchant)
    return redirect("/merchants")




# # DELETE
# # DELETE '/visits/<id>'
# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_task(id):
#     visit_repository.delete(id)
#     return redirect('/visits')