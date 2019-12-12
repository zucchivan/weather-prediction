from sqlalchemy import func, and_

from domain.city import City
from domain.prediction import Prediction
from ..database.orm_repository_base import RepositoryBase


class CityRepository(RepositoryBase):
    def __init__(self, db):
        super(CityRepository, self).__init__(db)

    def save(self, prediction):
        return super(CityRepository, self).save(prediction)

    def get_by_id(self, id):
        return self.session().query(City).filter_by(id=id).first()

    def get_highest_temperature(self, initial_date, final_date):
        return self.session().query(City.name, func.max(Prediction.temperature_max))\
            .join(City, Prediction.city_id == City.id).filter(and_(
                func.date(Prediction.prediction_date) >= initial_date),
                func.date(Prediction.prediction_date) <= final_date)\
            .group_by(City.id).all()
