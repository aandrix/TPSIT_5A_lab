from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

def validate(username, password):
    completion = False
    con = sqlite3.connect('./db.db')
    #with sqlite3.connect('static/db.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        if dbUser==username:
            completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

@app.route('/secret',methods=['GET', 'POST'])
def secret():
    print("ciao")
    if request.method == 'POST':
        if request.form.get('avanti1') == 'avanti':
            print("avanti")
            #ikmportare il comando avanti
        elif  request.form.get('indietro1') == 'indietro':
            print("indietro")
        elif  request.form.get('destra1') == 'destra':
            print("destra")
        elif  request.form.get('sinistra1') == 'sinistra':
            print("sinistra")
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')