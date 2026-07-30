import mysql.connector
from utilities.logger import Logger

class DatabaseUtility:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor= None
        self.logger = Logger.get_logger()


    def connect(self):
        print("Connecting to database...")
        try:
          self.connection = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
          print("Connection successful.")
          self.cursor = self.connection.cursor()
          self.logger.info("Database connection established successfully.")

        except Exception as e:
            print("Connection Failed:", e)
            self.logger.error(f"Database connection error: {e}")
            raise

    def execute_query(self,query):
        try:
           self.cursor.execute(query)
           self.logger.info(f"Query executed successfully: {query}")

        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            raise

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()

    def commit(self):
        try:
            self.connection.commit()
            self.logger.info(f"Transaction committed successfully.")

        except Exception as e:
            self.logger.error(f"Error while commiting transaction: {e}")
            raise

    def close_connection(self):
        try:
            if self.cursor:
             self.cursor.close()

            if self.connection:
             self.connection.close()

            self.logger.info("Database connection closed successfully.")
        except Exception as e:
            self.logger.error(f"Error while closing connection: {e}")
            raise


















