
class Car:

    def __init__(self, length=5, driver="basic"):
        self.location = 0
        self.length = length
        self.next_car = self
        self.driver = driver
        self.speed = 20

    def update(self, dt, road_length):
        self.location = (self.location + self.speed*dt) % road_length
