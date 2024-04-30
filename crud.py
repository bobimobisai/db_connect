create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price NUMERIC(10, 2) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        product_id INTEGER REFERENCES products(id),
        quantity INTEGER NOT NULL,
        total NUMERIC(10, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS customers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(20)
    )
    """,
]
import psycopg2

class ProductCRUD:
    def __init__(self, connection):
        self.connection = connection

    def create_product(self, name, price):
        query = "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (name, price))
                product_id = cursor.fetchone()[0]
                self.connection.commit()
                print("Product created with ID:", product_id)
                return product_id
        except psycopg2.Error as e:
            print("Error creating product:", e)
            return None

    def get_product(self, product_id):
        query = "SELECT * FROM products WHERE id = %s;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (product_id,))
                product = cursor.fetchone()
                return product
        except psycopg2.Error as e:
            print("Error retrieving product:", e)
            return None

    def update_product(self, product_id, name, price):
        query = "UPDATE products SET name = %s, price = %s WHERE id = %s;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (name, price, product_id))
                self.connection.commit()
                print("Product updated successfully.")
        except psycopg2.Error as e:
            print("Error updating product:", e)

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE id = %s;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (product_id,))
                self.connection.commit()
                print("Product deleted successfully.")
        except psycopg2.Error as e:
            print("Error deleting product:", e)

# Пример использования класса
conn_params = {
    "host": "87.242.103.6",
    "port": 5432,
    "dbname": "postgres",
    "user": "admin",
    "password": "admin123"
}

db_connection = psycopg2.connect(**conn_params)
product_crud = ProductCRUD(db_connection)

# Пример создания продукта
product_id = product_crud.create_product("Laptop", 999.99)

# Пример получения продукта по ID
product = product_crud.get_product(product_id)
print("Product:", product)

# Пример обновления продукта
product_crud.update_product(product_id, "New Laptop", 1099.99)

# Пример удаления продукта
product_crud.delete_product(product_id)

# Закрытие соединения с базой данных
db_connection.close()
