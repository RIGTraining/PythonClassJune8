# Drop Table 
import sqlite3
conn = sqlite3.connect('mydb1.db')
c = conn.cursor()
# Drop the table if it exists
c.execute('''
          DROP TABLE IF EXISTS contact
          ''')

conn.commit()  # save changes
conn.close()  # close the connection