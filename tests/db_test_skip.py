from utilities.db_utility import DatabaseUtility

def test_database_connection():

    db = DatabaseUtility(
        host="localhost",
        user="root",
        password="root123",
        database="testdb"
    )

    db.connect()

    db.execute_query("SELECT * FROM employee")

    result = db.fetch_all()

    print("Data:", result)

    assert result is not None

    db.close_connection()