import sqlite3

# f = open("Path", "w")
# text in file
conn = sqlite3.connect("Training.db")

c = conn.cursor()

# f.write
#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT,"+
          # "temperature REAL, date TEXT)")

# f = open("PATH", "r")
c.execute("SELECT time FROM iceCubeMelting")

# f.readline()
result = c.fetchone()
print(result)
result = c.fetchmany(size = 5) # print(c.arraysize)
print(result)
# f.read()
result = c.fetchall()
print(result)
# conn.commit()
c.close()
conn.close()