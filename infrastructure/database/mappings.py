from sqlalchemy import ForeignKey, Integer, String, Date, Text, DateTime
from sqlalchemy.orm import mapper, relationship
from domain.prediction import Prediction
from domain.city import City


def init(db):
    class TableCity(db.Model):
        __tablename__ = 'city'
        id = db.Column(String(20), primary_key=True)
        name = db.Column('name', String(255))
        state = db.Column('state', String(32))
        country = db.Column('country', String(32))

    class TablePrediction(db.Model):
        city_id = db.Column('city_id', Integer,
                            ForeignKey('city.id'),
                            nullable=False, primary_key=True)
        prediction_date = db.Column('prediction_date', Date, primary_key=True)
        rain_probability = db.Column('rain_probability', Integer)
        rain_precipitation = db.Column('rain_precipitation', Integer)
        temperature_min = db.Column('temperature_min', Integer)
        temperature_max = db.Column('temperature_max', Integer)
        city = relationship(City)

    db.mapper(City, TableCity.__table__)
    db.mapper(Prediction, TablePrediction.__table__)
