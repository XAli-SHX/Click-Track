from database import Database


class TrackerDatabase(Database):
    def __init__(self):
        super().__init__("tracker")
