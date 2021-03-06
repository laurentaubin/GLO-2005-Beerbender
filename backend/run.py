from flask import Flask, render_template, session
from flask_session import Session
from flask_cors import CORS
from blueprints import beers
from blueprints import home
from blueprints import signup
from blueprints import auth
from blueprints import customers
from blueprints import orders
from blueprints import brands
from blueprints import styles
from blueprints import types
from blueprints import rewards
from initialisation_script import createDatabaseScript, runAllInitScript

app = Flask(__name__,
                static_folder="./dist/static",
                template_folder="./dist")

CORS(app, resources={r"/*": {"origin": "*"}})

# Implementation from: https://hackersandslackers.com/flask-login-user-authentication/
# Implementation from: https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
def registerRoutes():
    app.register_blueprint(home.home)
    app.register_blueprint(beers.beers)
    app.register_blueprint(signup.signup_blueprint)
    app.register_blueprint(auth.login_blueprint)
    app.register_blueprint(customers.customers_blueprint)
    app.register_blueprint(orders.orders)
    app.register_blueprint(brands.brands)
    app.register_blueprint(styles.styles)
    app.register_blueprint(types.types)
    app.register_blueprint(rewards.rewards)

    return app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    createDatabaseScript('../database/db_init/create_database.sql')
    runAllInitScript()
    registerRoutes().run(debug=True)
