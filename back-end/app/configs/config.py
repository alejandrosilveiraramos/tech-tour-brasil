SECRET_KEY = "tech-tour-blumenau"

try:
    SQLALCHEMY_DATABASE_URI = \
        "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
        SGBD = "postgresql",
        usuario = "postgres",
        senha = "123456",
        servidor = "177.82.232.167",
        database = "techtour")
    print("Test connection: Online")

except Exception:
    print("Test connection: Offline")