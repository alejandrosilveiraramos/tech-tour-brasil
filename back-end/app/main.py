from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# --- Start Flask APP ---

app = Flask(
    __name__,
    template_folder='C:/Users/melissa.konig/Documents/aplicacao/tech-tour-brasil/back-end/app/static/components',
    static_folder='C:/Users/melissa.konig/Documents/aplicacao/tech-tour-brasil/back-end/app/static')

db = SQLAlchemy()


# --- DB connection ---

app.config.from_pyfile('./configs/config.py')

# --- Routes ---

from routes.routes  import *

# --- Main Running ---
if __name__ == "__main__":
    app.run(debug = True)
