# this is the "web_app/__init__.py" file...

from flask import Flask
from dotenv import load_dotenv
import os

from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes
from web_app.routes.stocks_routes import stocks_routes

# load variables in .env into environment
load_dotenv()

def create_app():
    app = Flask(__name__)

    # read secret key from environment
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_temp_key")

    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    app.register_blueprint(stocks_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)