'''

from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def front():
    request.method.g

    pass


if __name__ == '__main__':
    app.run(debug=True)


'''

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('avanti') == 'avanti':
            print("avanti")
        elif  request.form.get('indietro') == 'indietro':
            print("indietro")
        elif  request.form.get('destra') == 'destra':
            print("destra")
        elif  request.form.get('sinistra') == 'sinistra':
            print("sinistra")
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='localhost')