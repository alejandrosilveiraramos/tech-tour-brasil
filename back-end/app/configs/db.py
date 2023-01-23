import psycopg2

try:
    conn = psycopg2.connect(
    host = "177.82.232.167",
    port = "5432",
    database = "techtour", 
    user = "postgres", password = "123456")
    print("Db connection: Online")

except Exception:
    print("Db connection: Offline")

if conn is not None:
    
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE hotel (
                        hotel_id SERIAL,
                        hotel_name VARCHAR(64) NOT NULL,
                        hotel_city VARCHAR(64) NOT NULL,
                        hotel_coust DECIMAL(9,2) NOT NULL,
                      PRIMARY KEY (hotel_id));""")

    print("Hotel table created.")

    cursor.execute("""CREATE TABLE users (
                        user_id SERIAL,
                        user_lastName VARCHAR(64) NOT NULL,
                        user_firstName VARCHAR(64) NOT NULL,
                        user_gender BOOL NULL,
                        user_cpf VARCHAR(11) NOT NULL,
                        user_cep VARCHAR(8) NOT NULL,
                        user_phone VARCHAR(10) NULL,
                        user_cellphone VARCHAR(11) NOT NULL,
                        user_email VARCHAR(128) NOT NULL,
                        user_password VARCHAR(64) NOT NULL,
                      PRIMARY KEY (user_id));""")

    print("User table created.")

    cursor.execute("""CREATE TABLE history (
                        history_id SERIAL,
                        history_fk_id_user INT NOT NULL,
                        history_fk_id_hotel INT NOT NULL,
                        history_check_in DATE NULL,
                        history_check_out DATE NULL,
                      PRIMARY KEY (history_id),
                      FOREIGN KEY (history_fk_id_user)
                        REFERENCES users (user_id),
                      FOREIGN KEY (history_fk_id_hotel)
                        REFERENCES hotel (hotel_id));""")
        
    print("History table created.")

    conn.commit()
    cursor.close()
    conn.close()