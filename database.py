import json


class Database:
    def __init__(self, name: str):
        self.name = name + ".json"
        self.data = None

    def load(self):
        try:
            with open(self.name, 'r') as f:
                self.data = json.load(f)
                f.close()
        except IOError:
            pass

    def save(self):
        with open(self.name, 'w') as f:
            json.dump(self.data, f)
            f.close()

    def connect(self):
        self.load()

    def disconnect(self):
        self.save()
        self.data = None
