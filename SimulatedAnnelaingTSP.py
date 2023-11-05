from random import random
from random import shuffle
import numpy as np
from numpy.random import randint

class City:

    def __init__(self):
        self.x = 100 * random()
        self.y = 100 * random()

    def distance_to(self, city):

        dist_x = abs(self.x - city.x)
        dist_y = abs(self.y - city.y)

        return np.sqrt(dist_x*dist_x + dist_y*dist_y)

    def __repr__(self):
        return '(%s,%s)' % (self.x, self.y)


class SingleTour:

    def __init__(self, cities):
        self.cities = cities
        self.tour = []
        self.distance = 0
        self.generate_tour()

    def get_distance(self):

        if self.distance != 0:
            return self.distance

        tour_distance = 0

        for city_index in range(len(self.tour)):
            start_city = self.tour[city_index]

            if city_index+1 < len(self.tour):
                destination_city = self.tour[city_index+1]
            else:
                destination_city = self.tour[0]

            tour_distance += start_city.distance_to(destination_city)

        self.distance = tour_distance

        return self.distance

    def generate_tour(self):
        for city_index in range(len(self.cities)):
            self.tour[city_index] = self.cities[city_index]

        shuffle(self.tour)

    def get_tour_size(self):
        return len(self.tour)


class SimulatedAnnealing:

    # if the cooling rate is large - we consider just a few states in the search space
    # the cooling rate controls the number of states the algorithm will consider
    def __init__(self, cities, min_temp, max_temp, cooling_rate=0.02):
        self.cities = cities
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.cooling_rate = cooling_rate
        self.actual_state = SingleTour(cities)
        self.best_state = self.actual_state
        self.next_state = None

    def run(self):

        temp = self.max_temp

        while temp > self.min_temp:

            new_state = self.generate_random_state(self.actual_state)

            actual_energy = self.actual_state.get_distance()
            new_energy = new_state.get_distance()

            if random() < self.accept_prob(actual_energy, new_energy, temp):
                self.actual_state = new_state

            if self.actual_state.get_distance() < self.best_state.get_distance():
                self.best_state = self.actual_state

            temp = temp * (1-self.cooling_rate)

        print('Solution: %s' % self.best_state)

    # swap 2 cities at random
    def generate_random_state(self, actual_tour):

        new_state = SingleTour(self.cities)
        print(actual_tour.tour)
        new_state.tour = actual_tour.tour

        print(new_state.get_tour_size())

        random_index1 = randint(new_state.get_tour_size())
        random_index2 = randint(new_state.get_tour_size())

        city1 = new_state.tour[random_index1]
        city2 = new_state.tour[random_index2]

        new_state.tour[random_index1], new_state.tour[random_index2] = city2, city1

        return new_state

    @staticmethod
    def accept_prob(actual_energy, next_energy, temp):

        if next_energy > actual_energy:
            return 1

        return np.exp((actual_energy - next_energy) / temp)


if __name__ == '__main__':

    c = []

    for _ in range(100):
        c.append(City())

    algorithm = SimulatedAnnealing(c, 1, 100)
    algorithm.run()
