# importing required libraries
import mysql.connector


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="", database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None  # This will hold the actual connection
    
    def connect(self):
        if self.database:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        else:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

    def get_connection(self):
        if self.connection and self.connection.is_connected():
            return self.connection

