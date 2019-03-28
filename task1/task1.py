class Player(Account):
    def __init__(self):
        object_id_collector = self.id

class Bot(Account):
    def __init__(self):
        object_id_collector = self.id

class Tank(Vehicle):
    def __init__(self):
        object_id_collector = self.id

print Player().id, Player().id, Tank().id, Bot().id, Player().id
