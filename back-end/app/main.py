from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# --- Start Flask APP ---

app = Flask(
    __name__,
    template_folder='C:/python/tech-tour-brasil/back-end/app/static/components',
    static_folder='C:/python/tech-tour-brasil/back-end/app/static')

app.config.from_pyfile('./configs/config.py')

db = SQLAlchemy(app)


# --- DB connection ---



# --- Routes ---
#from routes.routes  import *
from views.view import *

# --- Main Running ---
if __name__ == "__main__":
    app.run(debug = True)
