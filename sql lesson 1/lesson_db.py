import psycopg2

conn = psycopg2.connect("host=87.242.103.6 port=5432 dbname=postgres user=admin password=admin123")

cur = conn.cursor()
user_id = 1
qwer = 'SELECT email FROM "user" WHERE id = %s;'
cur.execute(qwer, (user_id,))
res = cur.fetchone()
print(res)