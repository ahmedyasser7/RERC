import sqlite3


def WholeProgram():
    try:
        db = sqlite3.connect('properties.db')
        print("Connected")
        cr = db.cursor()
        cr.execute(
            "CREATE TABLE if not exists properties(id Integer Primary key autoincrement, Estate text, Area float, Date text, Price integer, Status text, Rooms integer, Location text"
        )
        cr.execute("INSERT INTO properties VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                   ())
        db.commit()
    except sqlite3.Error as er:
        print(f"Error! {er}")
    finally:
        if (db):
            db.close()


WholeProgram()
