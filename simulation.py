import random
import statistics as st
import numpy as np
from road import Road
from car import Car


class Simulation:

    def __init__(self, road, drivers, car_types, tick_interval=1):
        self.road = road
        self.drivers = drivers
        num_cars = int(self.road.length * 30 / 1000)
        random.shuffle(car_types)
        self.car_list = []
        total_cars = 0
        for percent_car in car_types:
            percent_car[0] = int(percent_car[0] * num_cars)
            total_cars += percent_car[0]
        for _ in range(num_cars - total_cars):
            car_types[random.randint(0, len(car_types) - 1)][0] += 1
        for car_count, car_class in car_types:
            for _ in range(car_count):
                self.car_list.append(car_class())
        random.shuffle(self.car_list)
        for position, car in enumerate(self.car_list):
            car.location = int(position * road.length / total_cars)
        self.tick_interval = tick_interval


    def run(self):
        pass

    def update(self):
        pass

    @property
    def current_positions(self):
        return [car.location for car in self.car_list]

    @property
    def current_speeds(self):
        return [car.speed for car in self.car_list]

