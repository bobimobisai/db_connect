import psycopg2

class PostgreSQLConnection:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            print("Connected to PostgreSQL!")
        except psycopg2.Error as e:
            print("Error: Could not connect to PostgreSQL:", e)

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection to PostgreSQL is closed.")

    def execute_query(self, query, params=None):
        try:
            with self.conn.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
                return result
        except psycopg2.Error as e:
            print("Error executing query:", e)
            return None

# Пример использования класса
conn_params = {
    "host": "87.242.103.6",
    "port": 5432,
    "dbname": "postgres",
    "user": "admin",
    "password": "admin123"
}

db_connection = PostgreSQLConnection(**conn_params)
db_connection.connect()

# Пример выполнения запроса
query = "SELECT * FROM users WHERE id = %s;"
params = (1,)
result = db_connection.execute_query(query, params)
print(result)

# Закрытие соединения с базой данных
db_connection.close()
