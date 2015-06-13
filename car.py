
class Car:

    def __init_(self, length=5, driver="basic"):
        self.location = 0
        self.length = length
        self.next_car = self
        self.driver = driver

    def update(self, dt):
        pass
