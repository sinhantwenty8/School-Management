import sqlite3

db = sqlite3.connect("studentdetail.sqlite")
'''db.execute("CREATE TABLE IF NOT EXISTS courseOffering(_id INTEGER PRIMARY KEY AUTOINCREMENT,coursename TEXT,student_id INTEGER DEFAULT 0,date TEXT DEFAULT CURRENT_TIMESTAMP,credittransferable TEXT DEFAULT FALSE)")
db.execute("INSERT INTO courseOffering (coursename, student_id,date,credittransferable) VALUES ('Bio','71','01-02-2021',TRUE)")
db.execute("INSERT INTO courseOffering (coursename, student_id,date,credittransferable) VALUES ('AddMath','72','09-03-2022',TRUE)")
'''


cursor = db.cursor()
cursor.execute("SELECT * FROM student")
for detail in cursor:
    print(detail)
cursor.execute("SELECT * FROM shortcourse")
for detail in cursor:
    print(detail)

cursor.close
cursor.connection.commit()
cursor.close
db.close
           
