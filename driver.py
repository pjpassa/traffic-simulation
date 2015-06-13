import random


class Driver:

    def __init__(self, name="basic", desired_speed=120, decel_chance=.1, accel_rate=2, decel_rate=2):
        self.desired_speed = desired_speed/3.6
        self.decel_chance = decel_chance
        self.accel_rate = accel_rate
        self.decel_rate = decel_rate
        self.name = name

    def __str__(self):
        return self.name

    def update(self, dt, car, road, speed_limit):
        front = car.location + car.length/2
        next_back = car.next_car.location - car.next_car.length/2
        if next_back < front:
            next_back += road.length
        if next_back - front < self.min_spacing(car):
            car.speed = car.next_car.speed
            return
        if random.random()*dt < self.decel_chance * road.get_decel_ratio(car.location):
            car.speed -= self.decel_rate
            return
        if car.speed < min([self.desired_speed, speed_limit]):
            car.speed = min((self.desired_speed, car.speed + self.accel_rate*dt))
            return

    def min_spacing(self, car):
        return car.speed
