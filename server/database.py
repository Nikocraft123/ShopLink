import sqlite3 as sql
import hashlib
import uuid


CREATE_USERS = """
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL COLLATE NOCASE,
        name TEXT UNIQUE NOT NULL COLLATE NOCASE,
        password TEXT NOT NULL,
        created INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
        admin INTEGER NOT NULL DEFAULT FALSE,
        bio TEXT
    )
"""


CREATE_SESSIONS = """
    CREATE TABLE IF NOT EXISTS Sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token TEXT UNIQUE NOT NULL,
        opened INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    )
"""


class Database:

    def __init__(self):

        print("Connect to database")
        self.conn = sql.connect("./database.db")

        c = self.conn.cursor()

        c.execute(CREATE_USERS)

        c.execute(CREATE_SESSIONS)

        self.conn.commit()

        c.execute("SELECT * FROM Users")
        print(c.fetchall())

        c.execute("SELECT * FROM Sessions")
        print(c.fetchall())

        c.close()

    def open_session(self, name_or_email: str, password: str) -> str:

        c = self.conn.cursor()

        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        c.execute("SELECT id FROM Users WHERE LOWER(name) LIKE LOWER(?) AND password LIKE ?",
                  (name_or_email, password_hash))
        user_by_name = c.fetchall()

        c.execute("SELECT id FROM Users WHERE LOWER(email) LIKE LOWER(?) AND password LIKE ?",
                  (name_or_email, password_hash))
        user_by_email = c.fetchall()

        if not (user_by_name or user_by_email):
            c.close()
            return ""

        token = uuid.uuid4()

        try:
            c.execute("""INSERT INTO Sessions
                (user_id, token)
                VALUES (?, ?)""", (1, token.hex))
        except sql.IntegrityError as error:
            if error.sqlite_errorcode != sql.SQLITE_CONSTRAINT_UNIQUE:
                raise
            return self.open_session(name_or_email, password)

        self.conn.commit()
        c.close()
        return token.hex

    def get_session(self, token: str) -> int:

        c = self.conn.cursor()

        c.execute("SELECT user_id FROM Sessions WHERE token LIKE ?",
                  (token,))
        user_id = c.fetchall()

        if not user_id:
            c.close()
            return 0

        return user_id[0]

    def close(self):

        print("Close database")
        self.conn.close()


db = Database()


if __name__ == "__main__":

    # password_hash = hashlib.sha256("1234".encode("utf-8")).hexdigest()
    # c.execute("INSERT INTO Users (email, name, password) VALUES (?, ?, ?)",
    #           ("hello@gmx.de", "Hello", password_hash))

    # print(open_session("hello@gmx.de", "1234"))
    print(db.get_session("055443d00b45435b8f20aa411ef5750d"))

    db.close()
