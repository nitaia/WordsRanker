import sqlite3

class Database:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def get(self, word):
        self.cursor.execute(f"SELECT * FROM words WHERE word = '{word}'")
        return self.cursor.fetchall()[0]

    def get_random(self):
        self.cursor.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 1")
        return self.cursor.fetchall()[0]

    def change_rank(self, word, amount):
        self.cursor.execute(f"UPDATE words SET rank = rank + {amount} WHERE word = '{word}'")
        self.db.commit()

    def get_top(self, amount):
        self.cursor.execute(f"SELECT * FROM words WHERE rank > 0 ORDER BY rank DESC LIMIT {amount}")
        return self.cursor.fetchall()