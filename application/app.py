from datetime import datetime

import requests
import json
import flask
from dateutil.parser import parse
from flask import Flask, jsonify, request
from application.config import Development

from application.exceptions import InvalidUsage, NoResultFound, ApplicationException
from domain.city import City
from domain.prediction import get_predictions_from_response_data
from infrastructure.database.context import Context

app = Flask(__name__)
app.config.from_object(Development)
context = Context(app)
context.setup()


@app.route('/info')
def info():
    return jsonify({
        'framework': 'Flask {}'.format(flask.__version__),
        'application': 'weather-prediction',
    })


@app.route('/cidade/<id_cidade>')
def weather_prediction_by_city(id_cidade):
    response = json.loads(requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'
                                       + id_cidade + '/days/15?token=' + app.config["CLIMATEMPO_TOKEN"]).text)
    if response.get('data') is None:
        raise NoResultFound('Nenhum registro encontrado para a cidade informada')

    city = context.city_repository.get_by_id(response.get('id'))

    if city is None:
        city = City(response.get('id'), response.get('name'), response.get('state'), response.get('country'))

    predictions = get_predictions_from_response_data(response)
    context.city_repository.save(city)
    context.prediction_repository.add_all(predictions)
    test = context.prediction_repository.get_by_city(response.get('id'))
    return 'dummy'


@app.route('/analise')
def weather_analysis():
    initial_date = datetime.strptime(request.args.get('data-inicial'), "%d-%m-%Y")
    final_date = datetime.strptime(request.args.get('data-final'), "%d-%m-%Y")
    highest_temperature = context.city_repository.get_highest_temperature(initial_date, final_date)
    average = context.prediction_repository.get_average_precipitation_by_city(initial_date, final_date)
    return 'dummer'


@app.errorhandler(ApplicationException)
def handle_application_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(Exception)
def handle_generic_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__app__':
    app.debug = True;
    app.run()
