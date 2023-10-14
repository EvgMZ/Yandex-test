import json
import random
import os


class Random_city():
    def __init__(self, path_to_file):
        self.dir_path = os.path.dirname(os.path.abspath(path_to_file))
        self.path = os.path.join(self.dir_path, path_to_file.split('/')[-1])

    def __read_json_file(self):
        try:
            with open(self.path) as file:
                self.data = json.load(file)
        except Exception as e:
            print(f'Error = {e}')

    def __get_sum_population(self):
        self.sum_population = 0
        self.count_city = 0
        for item in self.data:
            try:
                self.sum_population += item.get('population')
            except TypeError:
                print(f"In city {item['name']} Not found field population")

    def get_random_city(self):
        self.__read_json_file()
        self.__get_sum_population()
        r_number = random.random()
        compl = 0
        counter = 0
        while True:
            item = self.data[counter]
            people = item.get('population')
            if r_number < compl + people / self.sum_population:
                return item.get('name')
            compl += people / self.sum_population
            if counter == len(self.data) - 1:
                counter = 0
            else:
                counter += 1
