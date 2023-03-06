import sqlite3 as sql


db = sql.connect("./database.db")


def init():

    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS Users (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text UNIQUE NOT NULL,
            password text NOT NULL,
            created integer NOT NULL,
            rank integer NOT NULL DEFAULT 0,
            bio text
        )""")

    c.execute("""CREATE TABLE IF NOT EXISTS Sessions (
            id integer PRIMARY KEY AUTOINCREMENT,
            user_id integer NOT NULL,
            token text UNIQUE NOT NULL,
            created integer NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )""")

    #
    # c.execute("""INSERT INTO Users
    #     (name, password, created)
    #     VALUES (?, ?, ?)""", ("Nikocraft", "1234", 42))
    #
    # c.execute("""INSERT INTO Users
    #     (name, password, created)
    #     VALUES (?, ?, ?)""", ("Thejocraft", "abc", 1337))
    #
    # c.execute("""INSERT INTO Sessions
    #     (user_id, token, created)
    #     VALUES (?, ?, ?)""", (1, "this-is-a-long-token", 424242))
    #
    # c.execute("""INSERT INTO Sessions
    #     (user_id, token, created)
    #     VALUES (?, ?, ?)""", (1, "this-is-a-other-token", 12345678))
    #
    # db.commit()
    #
    # c.execute("SELECT * FROM Users")
    # print(c.fetchall())
    #
    # c.execute("SELECT * FROM Sessions")
    # print(c.fetchall())
    #
    # c.execute("""SELECT * FROM Users
    #     INNER JOIN Sessions ON Users.id = Sessions.user_id
    #     """)
    # print(c.fetchall())


def close():

    db.close()
