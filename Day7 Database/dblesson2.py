import sqlite3
# database connection
conn = sqlite3.connect('mydb1.db')
# open a database cursor
c = conn.cursor()
#retrieve data from the table
c.execute("SELECT * FROM contact")
rows = c.fetchall()  # fetch all rows from the executed query

for row in rows:
    print(f"Name: {row[1]}, Phone: {row[2]}, Address: {row[3]}")

conn.commit()  # save changes
conn.close()  # close the connection