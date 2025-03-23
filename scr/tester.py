from SQL_python_opgaver import DatabaseConnection
from SQL_python_opgave2 import Crud

# Create a connection to the database
db = DatabaseConnection(host="localhost", user="root", password="250404", database="orders_combined")

# Establish the connection
db.connect()  # This establishes the connection and doesn't return anything

# Get the connection object from DatabaseConnection
connection = db.get_connection()

if connection:  # Only proceed if the connection is valid
    crud = Crud(connection)

    # Perform a read operation (make sure the table and column exist)
    crud.read("orders_combined", "customer_name")

# Optional: Close the connection when done
#db.close_connection()



# mysql.connector.connect(
# host ="localhost",
# user ="root",
# passwd ="250404",
# database = "orders_combined"
# )