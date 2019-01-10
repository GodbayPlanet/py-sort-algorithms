class Utils:

    def __init__(self):
        pass

    @staticmethod
    def swap(items, i, j):
        temp = items[i]
        items[i] = items[j]
        items[j] = temp
