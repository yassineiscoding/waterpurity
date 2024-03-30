from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from waterpurity.pipeline.pipeline import PredictionPipeline

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/train', methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"


def prediction_message(prediction_value):
    if prediction_value < 0.6:
        return "This water sample is non-potable"
    else:
        return "This water sample is potable"


@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            ph = float(request.form['ph'])
            hardness = float(request.form['hardness'])
            solids = float(request.form['solids'])
            chloramines = float(request.form['chloramines'])
            sulfate = float(request.form['sulfate'])
            conductivity = float(request.form['conductivity'])
            organic_carbon = float(request.form['organic_carbon'])
            trihalomethanes = float(request.form['trihalomethanes'])
            turbidity = float(request.form['turbidity'])
            data = [ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes,
                    turbidity]
            data = np.array(data).reshape(1, -1)
            obj = PredictionPipeline()
            predict = obj.predict(data)
            message = prediction_message(predict[0])
            return render_template('results.html', prediction=message)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Failed to get values'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
