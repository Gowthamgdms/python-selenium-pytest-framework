print("Step 1")
from utilities.db_utility import DatabaseUtility
print("Step 2")

db = DatabaseUtility(
    host="localhost",
    user="root",
    password="root123",
    database="testdb"
)
print("Step 3")

db.connect()
print("Step 4")

db.execute_query("SELECT* FROM employee")
print("Step 5")

result = db.fetch_all()
print("Data:",result)

db.close_connection()
print("Step 6")