from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    sum = data['first'] + data['second']
    di = {}
    di['result'] = sum
    return di

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    sum = data['first'] - data['second']
    dic = {}
    dic['result'] = sum
    return dic

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
