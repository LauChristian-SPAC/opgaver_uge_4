class Crud:
    def __init__(self, connection):
        self.cursor = connection.cursor()
        self.connection = connection

    def create(self, table_name, *args):
        columns = ", ".join(args)
        query = f"CREATE TABLE {table_name} ({columns})"
        self.cursor.execute(query)

    def insert(self, table_name, **kwargs):
        columns = ", ".join(kwargs.keys())
        values = ", ".join(["%s"] * len(kwargs))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query, tuple(kwargs.values()))
        self.connection.commit()


    def read(self, table_name, *args):
        columns = ", ".join(args)
        query = f"SELECT {columns} FROM {table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for x in result:
            print(x)
        
    def update(self, table_name, new_value, old_value):
        query = f"UPDATE {table_name} SET {new_value} WHERE {old_value}"
        self.cursor.execute(query)
        self.connection.commit()
        rows_affected = self.cursor.rowcount
        if rows_affected > 0:
            print(f"Updated {rows_affected} row(s).")
        else:
            print("No rows were updated. Check the condition.")

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()