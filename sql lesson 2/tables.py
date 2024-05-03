tables_list = [
    """
    CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(264) NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS "user_info" (
    user_id INT PRIMARY KEY,
    name VARCHAR(264) NOT NULL,
    phone VARCHAR(64) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user" (id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS "orders" (
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    order_info VARCHAR(264),
    is_active BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES "user" (id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS "products" (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price NUMERIC(10, 2)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS "order_products" (
    order_id INT,
    product_id INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES "orders" (order_id),
    FOREIGN KEY (product_id) REFERENCES "products" (product_id)
    );
    """,
]
qwery_join = """
SELECT o.order_id, o.user_id, p.product_name FROM orders o
JOIN order_products op ON o.order_id = op.order_id
JOIN products p ON op.product_id = p.product_id
WHERE o.user_id = 1;
"""
qwery_group = """
SELECT o.user_id, SUM(p.price) AS total_price
FROM orders o
JOIN order_products op ON o.order_id = op.order_id
JOIN products p ON op.product_id = p.product_id
GROUP BY o.user_id;
"""


# INNER JOIN (Внутреннее объединение):
# INNER JOIN возвращает строки, которые имеют соответствующие значения в обеих таблицах, на которые ссылается JOIN.
# Если значения не совпадают, эти строки не включаются в результирующий набор.
# INNER JOIN используется, когда нужно получить только те строки, для которых есть совпадения в обеих таблицах.

# LEFT JOIN (или LEFT OUTER JOIN):
# LEFT JOIN возвращает все строки из левой таблицы (таблицы слева от JOIN) и соответствующие строки из правой таблицы 
# (таблицы справа от JOIN). Если для строки в левой таблице нет соответствующей строки в правой таблице, то значения 
# столбцов правой таблицы будут NULL.

# RIGHT JOIN (или RIGHT OUTER JOIN):
# RIGHT JOIN возвращает все строки из правой таблицы и соответствующие строки из левой таблицы. 
# Если для строки в правой таблице нет соответствующей строки в левой таблице, то значения столбцов левой таблицы будут NULL.

# FULL JOIN (или FULL OUTER JOIN):
# FULL JOIN возвращает все строки из обеих таблиц. Если для строки в одной из таблиц нет соответствующей строки в другой таблице,
# то значения столбцов для недостающих строк будут NULL.

# GROUP BY используется для группировки строк по значениям определенных столбцов. Это позволяет нам выполнять агрегатные функции
# (например, COUNT, SUM, AVG) на группах строк.

# HAVING:
# HAVING используется для фильтрации результатов, возвращенных GROUP BY, на основе агрегатных функций. Он выполняет ту же функцию, 
# что и WHERE, но на уже сгруппированных данных.
