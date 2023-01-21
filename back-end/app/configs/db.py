import psycopg2

print("Teste de conexão.")

try:
    conn = psycopg2.connect(
    host = "192.168.0.4",
    port ="5432",
    database = "techtour", 
    user="postgres", password = "123456")
    print("Conectado.")

except Exception:
    print("Você está sem conexâo.")

if conn is not None:
    
    print("Sua Conexão está estabilizada.")

    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE tb_hoteis (
                        id_hotel SERIAL,
                        name_hotel VARCHAR(45) NOT NULL,
                        city VARCHAR(45) NOT NULL,
                        coust DECIMAL(9,2) NOT NULL,
                      PRIMARY KEY (id_hotel));""")

    print("Tabela Hotel criada.")

    cursor.execute("""CREATE TABLE tb_users (
                        id_users SERIAL,
                        name VARCHAR(45) NOT NULL,
                        gender CHAR(1) NOT NULL,
                        cpf VARCHAR(11) NOT NULL,
                        cep VARCHAR(8) NOT NULL,
                        phone VARCHAR(45) NULL,
                        cellphone VARCHAR(45) NOT NULL,
                        email VARCHAR(45) NOT NULL,
                        password VARCHAR(45) NOT NULL,
                      PRIMARY KEY (id_users));""")

    print("Tabela Usuário criada.")

    cursor.execute("""CREATE TABLE tb_historic (
                        id_history SERIAL,
                        fk_id_users INT NOT NULL,
                        fk_id_hotel INT NOT NULL,
                        check_in DATE NULL,
                        check_out DATE NULL,
                      PRIMARY KEY (id_history),
                      FOREIGN KEY (fk_id_users)
                        REFERENCES tb_users (id_users),
                      FOREIGN KEY (fk_id_hotel)
                        REFERENCES tb_hoteis (id_hotel));""")
        
    print("Tabela Histórico criada.")

    conn.commit()
    cursor.close()
    conn.close()