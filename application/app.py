import requests
import json
import flask
from flask import Flask, jsonify
from domain.prediction import Prediction
from infrastructure.database.context import Context
from dateutil.parser import parse

app = Flask(__name__)
context = Context(app)
context.setup()


@app.route('/info')
def hello_world():
    return jsonify({
        'framework': 'Flask {}'.format(flask.__version__),
        'application': 'weather-prediction',
    })


@app.route('/cidade/<id_cidade>')
def weather_prediction_by_city(id_cidade):
    response = json.loads(requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'
                                       + id_cidade + '/days/15?token=b22460a8b91ac5f1d48f5b7029891b53').text)
    predictions = response.get('data')
    for p in predictions:
        rain = p.get('rain')
        temperature = p.get('temperature')
        date1 = parse(p.get('date'))
        prediction = Prediction(response.get('id'), parse(p.get('date')),
                                rain.get('probability'), rain.get('precipitation'),
                                temperature.get('min'), temperature.get('max'))
        context.prediction_repository.create(prediction)
    test = context.prediction_repository.get_for_city(response.get('id'))
    return 'dummy'


if __name__ == '__app__':
    app.debug = True;
    app.run()
