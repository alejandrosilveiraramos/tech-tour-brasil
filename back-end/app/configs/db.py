
import psycopg2

try:
    conn = psycopg2.connect(
    host = "192.168.0.4",
    port ="5432",
    database = "postgres", 
    user="postgres", password = "123456")
    print("Db connection: Online")

except Exception:
    print("Db connection: Offline")

if conn is not None:
    
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE tb_hotel (
                        id_hotel SERIAL,
                        name_hotel VARCHAR(64) NOT NULL,
                        city VARCHAR(64) NOT NULL,
                        coust DECIMAL(9,2) NOT NULL,
                      PRIMARY KEY (id_hotel));""")

    print("Hotel table created.")

    cursor.execute("""CREATE TABLE tb_user (
                        id_user SERIAL,
                        last_name VARCHAR(64) NOT NULL,
                        first_name VARCHAR(64) NOT NULL,
                            gender BOOL NULL,
                            cpf VARCHAR(11) NOT NULL,
                            cep VARCHAR(8) NOT NULL,
                            phone VARCHAR(10) NULL,
                            cellphone VARCHAR(11) NOT NULL,
                            email VARCHAR(128) NOT NULL,
                            password VARCHAR(64) NOT NULL,
                      PRIMARY KEY (id_user));""")

    print("User table created.")

    cursor.execute("""CREATE TABLE tb_history (
                        id_history SERIAL,
                        fk_id_user INT NOT NULL,
                        fk_id_hotel INT NOT NULL,
                        check_in DATE NULL,
                        check_out DATE NULL,
                      PRIMARY KEY (id_history),
                      FOREIGN KEY (fk_id_user)
                        REFERENCES tb_user (id_user),
                      FOREIGN KEY (fk_id_hotel)
                        REFERENCES tb_hotel (id_hotel));""")
        
    print("History table created.")

    conn.commit()
    cursor.close()
    conn.close()

