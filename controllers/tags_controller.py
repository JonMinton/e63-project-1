from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all() 
    merchants = merchant_repository.select_all()
    

    return render_template("/tags/index.html", 
                           tags = tags, 
                           merchants = merchants)

@tags_blueprint.route("/tags/new", methods = ['POST'])
def add_tag():
    print(request.form)
    merchant_id = request.form['merchant_id']
    print(f"merchant_id: {merchant_id}")
    new_tag = request.form['new_tag']
    tag = Tag(
        new_tag, 
        merchant_repository.select(merchant_id)
    )
    tag = tag_repository.save(tag)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/delete")
def delete_tag(id):
    tag_id = id
    tag_repository.delete(tag_id)
    return redirect("/tags")
