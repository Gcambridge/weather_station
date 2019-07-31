from flask import Flask, render_template, jsonify
from data import data_dict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    data = data_dict()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
