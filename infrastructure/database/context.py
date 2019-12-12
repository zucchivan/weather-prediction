class Context(object):

    def __init__(self, app):
        from flask_sqlalchemy import SQLAlchemy
        from infrastructure.database import mappings, prediction_repository, city_repository
        db = SQLAlchemy(app)
        mappings.init(db)
        self.db = db
        self.prediction_repository = prediction_repository.PredictionRepository(db)
        self.city_repository = city_repository.CityRepository(db)

    def setup(self):
        self.db.create_all()
