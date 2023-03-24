from flask import Flask, render_template

#  ################################################################
# Put controllers here : examples below
from controllers.tags_controller import tags_blueprint
# from controllers.authors_controller import authors_blueprint
# from controllers.books_controller import books_blueprint
# from controllers.authors_controller import authors_blueprint

app = Flask(__name__)

# Register controllers here. Examples below
app.register_blueprint(tags_blueprint)
# app.register_blueprint(books_blueprint)
# app.register_blueprint(authors_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
