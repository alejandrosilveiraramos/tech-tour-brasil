from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# --- Start Flask APP ---

app = Flask(__name__)

db = SQLAlchemy(app)

# --- DB connection ---

app.config.from_pyfile('./configs/config.py')

# --- Main Running ---
if __name__ == "__main__":
    app.run(debug = True)







