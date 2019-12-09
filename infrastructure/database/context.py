class Context(object):

    def __init__(self, app):
        from flask_sqlalchemy import SQLAlchemy
        from infrastructure.database import mappings, prediction_repository
        db = SQLAlchemy(app)
        mappings.init(db)
        self.db = db
        self.prediction_repository = prediction_repository.PredictionRepository(db)

    def setup(self):
        self.db.create_all()
