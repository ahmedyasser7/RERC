import sqlite3


class Prop():
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        self.cur.execute(
            "CREATE TABLE if not exists properties(id INTEGER PRIMARY KEY AUTOINCREMENT, Estate TEXT, Area INTEGER, Date TEXT, Price INTEGER, Status TEXT, Rooms INTEGER, Location TEXT)")
        self.con.commit()

    def insert(self, Estate, Area, Date, Price, Status, Rooms, Location):
        self.cur.execute("INSERT INTO properties VALUES (NULL,?,?,?,?,?,?,?)",
                         (Estate, Area, Date, Price, Status, Rooms, Location))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM properties")
        rows = self.cur.fetchall()
        return rows

    def remove(self, ID):
        self.cur.execute("DELETE FROM properties WHERE id=?", (ID,))
        self.con.commit()

    def update(self, ID, Estate, Area, Date, Price, Status, Rooms, Location):
        self.cur.execute("UPDATE properties SET Estate=?, Area=?, Date=?, Price=?, Status=?, Rooms=?, Location=? WHERE id=?",
                         (Estate, Area, Date, Price, Status, Rooms, Location, ID))
        self.con.commit()
