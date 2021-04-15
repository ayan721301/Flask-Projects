import pandas as pd
from flask import Flask, render_template, request, Response, url_for
from model import model
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    name = request.form.get("var_2", type=str)
    sharpe, stdev = model(name)
    return render_template('form.html', pred="{}".format(sharpe), pred2="{}".format(stdev))

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '_main_':
    app.run(debug=True)