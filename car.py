
class Car:

    def __init_(self, length=5, driver="basic"):
        self.location = 0
        self.length = length
        self.next_car = self
        self.driver = driver
        self.speed = 0

    def update(self, dt, road_length):
        self.location = (self.location + self.speed*dt) % road_length
