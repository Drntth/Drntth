import psycopg2

conn = psycopg2.connect(
    dbname="mydb", user="myuser", password="mypassword", host="localhost"
)
cur = conn.cursor()
# Parameterized query prevents SQL injection
cur.execute("SELECT * FROM employees WHERE name = %s;", ("Alice",))
print(cur.fetchall())
cur.close()
conn.close()
