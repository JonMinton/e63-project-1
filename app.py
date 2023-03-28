from flask import Flask, render_template

#  ################################################################
# Put controllers here : examples below
from controllers.merchants_controller import merchants_blueprint
from controllers.customers_controller import customers_blueprint
from controllers.accounts_controller import accounts_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.tags_controller import tags_blueprint

import repositories.customer_repository as customer_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.account_repository as account_repository
import repositories.transaction_repository as transaction_repository

app = Flask(__name__)

# Register controllers here. Examples below
app.register_blueprint(merchants_blueprint)
app.register_blueprint(customers_blueprint)
app.register_blueprint(accounts_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(tags_blueprint)

@app.route('/')
def home():

    customers = customer_repository.select_all()
    n_customers = len(customers)

    tags = tag_repository.select_all()
    n_tags = len(tags)

    merchants = merchant_repository.select_all()
    n_merchants = len(merchants)
    n_merchant_sales = sum([x.num_sales for x in merchants])
    total_merchant_revenue = sum([x.revenue for x in merchants])

    accounts = account_repository.select_all()
    n_accounts = len(accounts)
    total_balance = sum([x.balance for x in accounts])

    transactions = transaction_repository.select_all()
    n_transactions = len(transactions)
    total_transaction_value = sum([x.amount for x in transactions])

    return render_template(
        'index.html',
        n_customers = n_customers,
        n_tags = n_tags,

        n_merchants = n_merchants,
        n_merchant_sales = n_merchant_sales,
        total_merchant_revenue = total_merchant_revenue,

        n_accounts = n_accounts,
        total_balance = total_balance,

        n_transactions = n_transactions,
        total_transaction_value = total_transaction_value
        )

if __name__ == '__main__':
    app.run(debug=True)
