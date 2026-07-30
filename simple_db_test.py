import mysql.connector

print("Starting...")

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root123",
        database="testdb",
        connection_timeout=5
    )

    print("Connected Successfully")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")

    print(cursor.fetchall())

    cursor.close()
    conn.close()

except Exception as e:
    print(e)