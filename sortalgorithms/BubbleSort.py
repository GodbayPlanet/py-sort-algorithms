from Utils import Utils


class BubbleSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(items):
        for i in range(0, len(items) - 1):
            for j in range(0, len(items) - i - 1):
                if items[j + 1] < items[j]:
                    Utils.swap(items, j + 1, j)
        return items
