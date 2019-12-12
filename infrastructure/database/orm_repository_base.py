class RepositoryBase(object):
    def __init__(self, db):
        self.db = db

    def session(self):
        return self.db.session

    def save(self, item):
        item = self.session().merge(item)
        self.session().add(item)
        self.session().commit()

    def add_all(self, items):
        for item in items:
            self.save(item)
