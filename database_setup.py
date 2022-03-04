import sqlite3

def first_init():
    con = sqlite3.connect('words.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS words
                        (word text PRIMARY KEY, rank integer)''')


    file = open('words.txt')
    for word in file:
        cur.execute(f"INSERT OR IGNORE INTO words VALUES ('{word[:-1]}', '0')")
    
    con.commit()

if __name__ == '__main__':
    first_init()
