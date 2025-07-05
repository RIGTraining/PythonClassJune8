import sqlite3
conn = sqlite3.connect('mydb1.db')
c = conn.cursor()

# Delete data from the table
c.execute('''
          DELETE FROM contact WHERE id = 4
          ''')


conn.commit()  # save changes
conn.close()  # close the connection

