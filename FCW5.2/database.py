import psycopg2
from psycopg2 import Error

class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except (Exception, Error) as error:
            print(f"Ошибка подключения к базе данных: {error}")
            self.connection = None

    def create_table(self):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS home_animals (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS pets (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        animal_id INT REFERENCES home_animals(id),
                        commands TEXT[]
                    );
                    INSERT INTO home_animals (name)
                        VALUES ('Кошка'),
                               ('Собака'),
                               ('Хомяк');

                    """)
                    self.connection.commit()
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)

    def close(self):
        if self.connection:
            self.connection.close()