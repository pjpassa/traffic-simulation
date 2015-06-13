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

    def update(self, dt, car, road):
        if (car.next_car.location + road.length) % road.length - car.location < self.min_spacing(car):
            car.speed = car.next_car.speed
            return
        if random.random()*dt < self.decel_rate * road.get_decel_ratio(car.location):
            car.speed -= self.decel_rate*dt
            return
        if car.speed < self.desired_speed:
            car.speed = min((self.desired_speed, car.speed + self.accel_rate*dt))
            return

    def min_spacing(self, car):
        return car.speed