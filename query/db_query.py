"""
This file contains mysql insert for the database we created.
Author: Rutuja Tikhile.
Date:29/3/2020
"""
from config.mysql_connection import con


class Query:  # Data access layer

    def __init__(self):
        self.mydb = con

    # Dynamic insert query for inserting data into the specific table of database.
    def insert(self, data, table_name):
        column = []
        rows_values = []
        val = []
        for key, value in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(value)
        print(column)
        print(rows_values)
        print(val)
        column = ','.join(column)
        val_ = ','.join(['%s'] * len(val))
        query = f'''INSERT INTO %s (%s) VALUES (%s)''' % (table_name, column, val_)
        self.mydb.query_execute(query=query, value=val)

    # def insert_many(self,data, table_name):
    #
    #     sql = f"insert into {table_name} (id, text) values(%s,%s)"
    #     val = data
    #     self.mydb.query_execute(sql,val)

    # def insert_many(self,data, table_name):
    #
    #     sql = f"insert into {table_name} (title, link, para) values(%s,%s,%s)"
    #     val = data
    #     self.mydb.query_execute(sql,val)

    def insert_many(self,data, table_name):

        sql = f"insert into {table_name} (title, description, link, image) values(%s,%s,%s,%s)"
        val = data
        self.mydb.query_execute(sql,val)