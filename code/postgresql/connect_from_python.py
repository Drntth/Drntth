import psycopg2
from psycopg2 import sql

# 1. Connect using parameters
conn = psycopg2.connect(
    dbname="mydb", user="myuser", password="mypassword", host="localhost"
)

# 2. Connect using a connection string
# conn = psycopg2.connect("dbname=mydb user=myuser password=mypassword host=localhost")

# 3. Connect using environment variables (if set)
# conn = psycopg2.connect("")

cur = conn.cursor()

# Simple SELECT query
cur.execute("SELECT version();")
print(cur.fetchone())

# Parameterized SELECT query (safer)
cur.execute("SELECT * FROM employees WHERE name = %s;", ("Alice",))
print(cur.fetchall())

# Insert multiple rows
cur.executemany(
    "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s);",
    [("Carol", "Analyst", 60000), ("Dave", "Designer", 65000)]
)

# UPDATE operation
cur.execute("UPDATE employees SET salary = salary + 1000 WHERE name = %s;", ("Alice",))

# DELETE operation
cur.execute("DELETE FROM employees WHERE name = %s;", ("Dave",))

# DDL operation (e.g., create table)
cur.execute("""
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        data TEXT
    );
""")

# Dynamic SQL using the sql module
table_name = "employees"
cur.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name)))
print(cur.fetchall())

cur.close()
conn.commit()
conn.close()