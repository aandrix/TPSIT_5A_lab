import sqlite3
def check_password(hashed_password, user_password):
    return hashed_password == user_password
def validate(username, password):
    completion = False
    con = sqlite3.connect('./db.db')
    #with sqlite3.connect('static/db.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    rows = cur.fetchall()
    for row in rows:#controllo tutte le ricghe del db 
        dbUser = row[0]
        dbPass = row[1]
        if dbUser==username:
            completion=check_password(dbPass, password)
    
    return completion


utente = "Zoassa"

psw = "123456"
print(validate(utente, psw))
