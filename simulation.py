import random
import statistics as st
import numpy as np
from road import Road
from car import Car


class Simulation:

    # car_types example = [[1, Car, 5, "basic"]]
    def __init__(self, road, drivers, car_types, tick_interval=1):
        self.road = road
        self.drivers = {str(driver): driver for driver in drivers}
        num_cars = int(self.road.length * 30 / 1000)
        random.shuffle(car_types)
        self.car_list = []
        total_cars = 0
        for percent_car in car_types:
            percent_car[0] = int(percent_car[0] * num_cars)
            total_cars += percent_car[0]
        for _ in range(num_cars - total_cars):
            car_types[random.randint(0, len(car_types) - 1)][0] += 1
        for car_count, car_class, car_length, car_driver in car_types:
            for _ in range(car_count):
                self.car_list.append(car_class(car_length, car_driver))
        random.shuffle(self.car_list)
        for position, car in enumerate(self.car_list):
            car.location = int(position * road.length / total_cars)
            car.next_car = self.car_list[(position + 1) % len(self.car_list)]
        self.tick_interval = tick_interval

    def run(self, time=60):
        speeds = np.array([self.current_speeds])
        states = np.array([self.current_positions])
        times = [0]
        for i in range(int(time/self.tick_interval)):
            self.update()
            speeds = np.vstack((speeds, self.current_speeds))
            states = np.vstack((states, self.current_positions))
            times.append((i + 1) * self.tick_interval)
        return (speeds, states, times)

    def update(self):
        # update speeds
        for car in self.car_list:
            self.drivers[car.driver].update(self.tick_interval, car, self.road)
        # move cars
        for car in self.car_list:
            car.update(self.tick_interval, self.road.length)

    @property
    def current_positions(self):
        return [car.location for car in self.car_list]

    @property
    def current_speeds(self):
        return [car.speed for car in self.car_list]
