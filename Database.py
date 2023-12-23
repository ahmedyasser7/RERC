import sqlite3


class Database():
    def __init__(self, db):

        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        self.cur.execute(
            "CREATE TABLE if not exists properties(id Integer Primary key autoincrement, Estate text, Area float, Date text, Price integer, Status text, Rooms integer, Location text")
        self.con.commit()

    def insert(self, Estate, Area, Date, Price, Status, Rooms, Location):
        self.cur.execute("insert into student values (NULL,?,?,?,?,?,?,?)",
                         (Estate, Area, Date, Price, Status, Rooms, Location))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        return rows

    def remove(self, ID):
        self.cur.execute("delete from student where id=?", (ID,))
        self.con.commit()

    def update(self, ID, Estate, Area, Date, Price, Status, Rooms, Location):
        self.cur.execute("update student set name=?,gpa=?,email=?,section=?,level=?,address=? where id=?",
                         (Estate, Area, Date, Price, Status, Rooms, Location, ID))
        self.con.commit()
