from sqlalchemy import ForeignKey, Integer, String, Date, Text, DateTime
from sqlalchemy.orm import mapper, relationship
from domain.entities import *


def init(db):
    city_mapping = db.Table('city',
                            db.Column('id', String(20), primary_key=True),
                            db.Column('name', String(255)),
                            db.Column('state', String(32)),
                            db.Column('country', String(32)),
                            )

    prediction_mapping = db.Table('prediction',
                                  db.Column('city_id', Integer,
                                            ForeignKey("city.id", onupdate="CASCADE", ondelete="CASCADE"),
                                            nullable=False, primary_key=True),
                                  db.Column('prediction_date', Date, primary_key=True),
                                  db.Column('rain_probability', Integer),
                                  db.Column('rain_precipitation', Integer),
                                  db.Column('temperature_min', Integer),
                                  db.Column('temperature_max', Integer)
                                  )

    db.mapper(City, city_mapping)
    db.mapper(Prediction, prediction_mapping)
