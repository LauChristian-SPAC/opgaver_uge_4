from SQL_python_opgaver import DatabaseConnection
import pandas as pd

    # --- create table orders_combined ---
data = pd.read_csv("data/orders_combined.csv")
db = DatabaseConnection(host="localhost", user="root", password="250404", database="orders_combined")
db.connect()
connection = db.get_connection()
cursorObject = connection.cursor()

orders_combined_table = """CREATE TABLE orders_combined (
id INT,
date_time VARCHAR(50),
customer_name VARCHAR(50),
customer_email VARCHAR(50),
product_name VARCHAR(50),
product_price FLOAT
)"""

cursorObject.execute(orders_combined_table)

for index, row in data.iterrows():
    cursorObject.execute(
        "INSERT INTO orders_combined (id, date_time, customer_name, customer_email, product_name, product_price) VALUES (%s, %s, %s, %s, %s, %s)",
        (row['id'], row['date_time'], row['customer_name'], row['customer_email'], row['product_name'], row['product_price'])
    )

connection.commit()
