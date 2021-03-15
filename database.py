import sqlite3

from sqlite3 import Error

"""
    Create database for project
"""

class DataBase:

    def __init__(self):
        # Create a database object
        
        try:
            self.db = sqlite3.connect('server.db')
            self.cursor = self.db.cursor()
        
        except Error:
            print('Emerged Error')
            

    def create_new_table(self):   
        # Create a table with four columns
        self.cursor.execute("CREATE TABLE Exchange_Rate(id integer PRIMARY KEY, date_ TEXT, time_ TEXT, rate_ BIGINT)")
        self.db.commit()

    def write_to_table(self, entities):
        # Write data to table
        self.cursor.execute('INSERT INTO Exchange_Rate(id, date_, time_, rate_) VALUES(?, ?, ?, ?)', entities)
        self.db.commit()

    def update_table(self):
        # Update data in table
        self.cursor.execute('UPDATE Exchange_Rate SET rate_ = 777 WHERE id = 1')
        self.db.commit()

    def count_id(self):
        self.cursor.execute('SELECT id FROM Exchange_Rate')
        self.c_id = self.cursor.fetchall()

# entities = (id, date_request, time_request, rate)

# manager = DataBase()
# manager.sql_connection()
# manager.create_new_table()
# manager.write_to_table(entities)
# manager.update_table()
