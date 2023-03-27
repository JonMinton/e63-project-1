from flask import Flask, render_template

#  ################################################################
# Put controllers here : examples below
# from controllers.tags_controller import tags_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.customers_controller import customers_blueprint
from controllers.accounts_controller import accounts_blueprint
from controllers.transactions_controller import transactions_blueprint

app = Flask(__name__)

# Register controllers here. Examples below
app.register_blueprint(merchants_blueprint)
app.register_blueprint(customers_blueprint)
app.register_blueprint(accounts_blueprint)
app.register_blueprint(transactions_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
