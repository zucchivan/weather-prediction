import datetime
from sqlalchemy import desc
from domain.entities import Prediction
from ..database.orm_repository_base import RepositoryBase


class PredictionRepository(RepositoryBase):
    def __init__(self, db):
        super(PredictionRepository, self).__init__(db)

    def create(self, prediction):
        return super(PredictionRepository, self).create(prediction)

    def get_for_city(self, city_id):
        return self.session().query(Prediction).filter_by(city_id=city_id).order_by(desc("prediction_date")).all()
