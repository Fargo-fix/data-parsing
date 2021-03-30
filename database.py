import sqlite3

from sqlite3 import Error

"""
    Create database for project
"""

class DataBase:
    # Create a database object
    def __init__(self):

        
        try:
            self.db = sqlite3.connect('server.db')
            self.cursor = self.db.cursor()
        
        except Error:
            print('Emerged Error')
            
    # Create a table with four columns
    def create_new_table(self):   
        
        self.cursor.execute("CREATE TABLE Exchange_Rate(id integer PRIMARY KEY, date_ TEXT, time_ TEXT, rate_ BIGINT)")
        self.db.commit()

    # Write data to table
    def write_to_table(self, entities):
        
        self.cursor.execute('INSERT INTO Exchange_Rate(id, date_, time_, rate_) VALUES(?, ?, ?, ?)', entities)
        self.db.commit()

    # Update data in table
    def update_table(self):
        
        self.cursor.execute('UPDATE Exchange_Rate SET rate_ = 777 WHERE id = 1')
        self.db.commit()

    # Count id lines
    def count_id(self):
        
        self.cursor.execute('SELECT id FROM Exchange_Rate')
        self.c_id = self.cursor.fetchall()

    # Get all rate values
    def get_rate(self):

        self.cursor.execute('SELECT rate_ FROM Exchange_Rate')
        self.all_rate_values = self.cursor.fetchall()
    # Get all date values
    def get_date(self):

        self.cursor.execute('SELECT date_ FROM Exchange_Rate')
        self.all_date_values = self.cursor.fetchall()