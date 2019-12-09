import datetime


class Prediction:
    def __init__(self, city_id: int, prediction_date: datetime, rain_probability: int, rain_precipitation: int,
                 temperature_min: int, temperature_max: int):
        self.city_id = city_id
        self.prediction_date = prediction_date
        self.rain_probability = rain_probability
        self.rain_precipitation = rain_precipitation
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
