
import AlphaBot 
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('avanti1') == 'avanti':
            print("avanti")
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')