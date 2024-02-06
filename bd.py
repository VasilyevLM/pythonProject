import sqlite3

connection = sqlite3.connect('mydb.db')
cur = connection.cursor()



user = [
    ('Ivan', 'Ivanov', 'male'),
    ('Mariya', 'Ivanova', 'female'),
    ('Boris', 'Petrov', 'male')
]

def db_create():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    gender TEXT);
    """)
    connection.commit()


def add_user(user):


    cur.executemany("""INSERT INTO users(fname, lname, gender) 
       VALUES(?, ?, ?);""", user)
    connection.commit()

def get_user():
    data = cur.execute("""SELECT * FROM users""")
    print(data.fetchall())


def update_user():
    cur.execute("""UPDATE users SET fname = 'Alina' WHERE userid = 2""")
    connection.commit()


# db_create()
# add_user(user)
# get_user()
update_user()
connection.close()