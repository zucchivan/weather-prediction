from sqlalchemy import desc, select, func, and_
from domain.prediction import Prediction
from domain.city import City
from ..database.orm_repository_base import RepositoryBase


class PredictionRepository(RepositoryBase):
    def __init__(self, db):
        super(PredictionRepository, self).__init__(db)

    def save(self, prediction):
        return super(PredictionRepository, self).save(prediction)

    def get_by_city(self, city_id):
        return self.session().query(Prediction).filter_by(city_id=city_id).order_by(desc("prediction_date")).all()

    def get_average_precipitation_by_city(self, initial_date, final_date):
        return self.session().query(City.name, func.avg(Prediction.rain_precipitation))\
            .join(City, Prediction.city_id == City.id).filter(and_(
                func.date(Prediction.prediction_date) >= initial_date),
                func.date(Prediction.prediction_date) <= final_date)\
            .group_by(City.id).all()
