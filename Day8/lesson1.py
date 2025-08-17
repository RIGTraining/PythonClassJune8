#sqlite3
import sqlite3
# Flask Web Framework
# pip install flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
conn = sqlite3.connect('mydb.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT,
            email TEXT)
          ''')




@app.route('/')
def homepage():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact")
    rows = c.fetchall()  # fetch all rows from the executed query

    return render_template('home.html', kname = rows)

@app.route('/home2')
def home2():
    return render_template('home2.html')
    
@app.route('/save', methods=('GET','POST'))
def save_data():
    n = request.args.get('cname')
    p = request.args.get('phone')
    a = request.args.get('address')
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO contact(name, phone, address) VALUES(?,?,?)",(n,p,a))
    
    conn.commit()#save changes
    conn.close()#close the connection

    return redirect('/')

@app.route('/delete/<int:id>', methods=('GET','POST'))
def delete_data(id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    # c.execute("DELETE FROM contact WHERE id = 2")
    
    c.execute("DELETE FROM contact WHERE id = ?", (id,))
    conn.commit()#save changes
    conn.close()#close the connection
    
    return redirect('/')

@app.route('/edit/<int:id>', methods=('GET','POST'))
def edit_data(id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact WHERE id =?", (id,))
    rows = c.fetchone()
    return render_template('edit.html', row=rows)   

@app.route('/editdata/<int:id>', methods=('GET','POST'))
def update_data(id):
    n = request.args.get('cname')
    p = request.args.get('phone')
    a = request.args.get('address')
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("update contact set name=?, phone=?, address=? where id=?",  (n,p,a, id))
    conn.commit()#save changes
    conn.close()#close the connection
    
    return redirect('/')
    

conn.commit()#save changes
conn.close()#close the connection

if __name__ == '__main__':
    app.run()