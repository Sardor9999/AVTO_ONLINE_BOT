import psycopg2

def select_all_user():
    connection= psycopg2.connect(
        user="postgres",
        password="pynative@#29",
        host="127.0.0.1",
        port="5432",
        database="postgres"
        )
    cursor = connection.cursor()
    sql1="""CREATE TABLE Category(
        id SERIAL NOT NULL ,
        title VARCHAR(50)
        );"""

    sql2 = """CREATE CAR Category(
            id SERIAL NOT NULL ,
            title VARCHAR(50),
            description TEXT NOT NULL,
            image_url VARCHAR(250) NOT NULL,
            price NUMERIC NOT NULL,
            cat_id INTEGER NOT NULL
            );"""
    cursor.execute(sql1)
    cursor.execute(sql2)
    connection.commit()
    cursor.close()
    connection.close()

# create_table()