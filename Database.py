import json


class Database:
    def __init__(self, name: str):
        self.name = name

    def load(self):
        with open(self.name, 'r') as f:
            db = json.load(f)
            f.close()
            return db

    def save(self, database):
        with open(self.name, 'w') as f:
            json.dump(database, f)
            f.close()

    def connect(self):
        return self.load()

    def disconnect(self, database):
        self.save(database)
