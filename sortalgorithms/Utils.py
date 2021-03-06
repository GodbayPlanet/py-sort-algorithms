import random


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def swap(items, i, j):
        temp = items[i]
        items[i] = items[j]
        items[j] = temp

    @staticmethod
    def get_numbers():
        return [4, 3, 2, 1, 9, 10, 7, 8, 6]

    @staticmethod
    def get_characters():
        return ['f', 'b', 'a', 'd', 'h', 'c']

    @staticmethod
    def get_strings():
        return ["Quit", "Practice", "Logs", "Coding", "Array"]

    @staticmethod
    def get_random_numbers_of_length(array_length):
        return [random.randint(1, 10) for _ in range(array_length)]
