from flask import Flask, render_template, make_response, redirect, url_for, request, jsonify

import AlphaBot
app = Flask(__name__)
robot = AlphaBot.AlphaBot()


@app.route("/api/v1/sensoreSx")
def senzore1():
    return jsonify (robot.getProssimitySensors("sinistra"))

@app.route("/api/v1/sensoreDx")
def senzore2():
    return jsonify (robot.getProssimitySensors("destra"))

@app.route("/api/v1/sensore")
def senzore3():
    if "dir" in request.args:
        if request.args["dir"] == "sinistra":
            return jsonify(robot.getProssimitySensors("sinistra"))
        elif request.args["dir"] == "destra":
            return jsonify(robot.getProssimitySensors("destra"))
        elif request.args["dir"] == "all":
            tupla = robot.getProssimitySensors("entrambi")
            diz = {"sinistra": tupla[0], "destra": tupla[1]}
            return jsonify(diz)
        
@app.route('/')
def home():
    return render_template('index.html')
        
  


if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')