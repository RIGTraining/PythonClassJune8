import sqlite3
# database connection 
conn = sqlite3.connect('mydb1.db')
#open a database cursor
c = conn.cursor()
# create a table
c.execute('''
          CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT)
          ''')

#inseting data into the table
c.execute('''
          INSERT INTO contact(name, phone, address)
          VALUES('Aung Aung', '1234567890', 'Yangon')
          ''')

c.execute('''
          INSERT INTO contact(name, phone, address)
          VALUES('Kyaw Kyaw', '1234567890', 'Mandalay')
          ''')

conn.commit()#save changes
conn.close()#close the connection