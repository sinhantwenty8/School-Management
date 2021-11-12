import sqlite3

db = sqlite3.connect("studentdetail.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS enrolcourse(name TEXT,coursename TEXT)")
cursor = db.cursor()

cursor.execute("SELECT * FROM shortcourse")



for detail in cursor:
    print(detail)
cursor.connection.commit()
cursor.close
db.close
           
