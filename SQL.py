import sqlite3

# f = open("Path", "w")
# text in file
conn = sqlite3.connect("Training.db")

c = conn.cursor()

# f.write
#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT,"+
          # "temperature REAL, date TEXT)")

c.execute("SELECT time FROM iceCubeMelting")
# conn.commit()
c.close()
conn.close()