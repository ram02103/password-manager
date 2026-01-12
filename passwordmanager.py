import sqlite3
conn=sqlite3.connect("manager.db")
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS passwords(id INTEGER PRIMARY KEY,
             site TEXT,
            username TEXT,
            password TEXT)""")
conn.commit()
def save_password(site,username,password):
    cur.execute("INSERT INTO passwords(site,username,password)VALUES(?,?, ?)",(site,username,password))
    conn.commit()
def get_passwords():
    cur.execute("SELECT site, username, password FROM passwords")
    return cur.fetchall()
save_password("gmail","karthikeya2321@gmail.com",12345)
print(get_passwords())
conn.close()


