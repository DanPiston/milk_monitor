import sqlite3

MILKDB = 'milk.db'

class MilkLogEntry(object):
    def __init__(self, starting_ounces):
        self.starting_ounces = float(starting_ounces)

    def set_ending_ounces(self, ounces):
        self.ending_ounces = float(ounces)
        
    @property
    def amount_consumed(self):
        return self.starting_ounces - self.ending_ounces

    def log_db(self, starting_ounces, ending_ounces, total_ounces):
        connection = sqlite3.connect(MILKDB)
        sql = """insert into milk_table values (
                 :starting_ounces, :ending_ounces, :total_ounces)"""
        args = {
                'starting_ounces':starting_ounces,
                'ending_ounces':ending_ounces,
                'total_ounces':total_ounces}
        connection.execute(sql, args)
        connection.commit()
        print('DB has been updated!')
