from flask import Flask, render_template, request, jsonify
import random 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a', methods=['GET', 'POST'])
def button_a():
    if request.method == 'POST':
        print("A")
    return render_template('index.html')

@app.route('/b', methods=['GET', 'POST'])
def button_b():
    if request.method == 'POST':
        print("B")
    return render_template('index.html')

@app.route('/api')
def random_number():
    return jsonify({"o": random.randint(0, 1)})

if __name__ == '__main__':
    app.run(debug=True)
