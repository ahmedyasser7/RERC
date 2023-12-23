import sqlite3


def connect_db():
    conn = sqlite3.connect('OwmerData.db')
    return conn


con = connect_db()
cursor = con.cursor()
cursor.execute(
    "Drop OwnerData"
)
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (1, 123))
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (2, 456))
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (3, 789))
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (4, 2468))
con.commit()
con.close()
