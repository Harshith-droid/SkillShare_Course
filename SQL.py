import sqlite3

conn = sqlite3.connect("Training.db")
c = conn.cursor()

f

# f.write
#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT,"+
          # "temperature REAL, date TEXT)")

c.close()
conn.close()