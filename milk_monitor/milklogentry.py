import sqlite3
import time

MILKDB = 'milk.db'

class MilkLogEntry(object):
    def __init__(self, starting_ounces):
        self.starting_ounces = float(starting_ounces)

    def set_ending_ounces(self, ounces):
        self.ending_ounces = float(ounces)
        
    @property
    def amount_consumed(self):
        return self.starting_ounces - self.ending_ounces

    def log_db(self):
        connection = sqlite3.connect(MILKDB)
        sql = """insert into milked values (
                 :starting_ounces, :ending_ounces, :total_ounces, :time)"""
        args = {
                'starting_ounces':self.starting_ounces,
                'ending_ounces':self.ending_ounces,
                'total_ounces':self.amount_consumed,
                'time':time.strftime('%Y-%m-%d %H:%M:%S')}
        connection.execute(sql, args)
        connection.commit()
        print('DB has been updated!')
