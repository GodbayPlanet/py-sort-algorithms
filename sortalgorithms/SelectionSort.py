from Utils import Utils


class SelectionSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(items):
        for i in range(0, len(items)):
            current_minimum = SelectionSort.__get_min_element_index(i, items)
            if items[current_minimum] < items[i]:
                Utils.swap(items, i, current_minimum)

        return items

    @staticmethod
    def __get_min_element_index(index, items):
        min_index = index

        for i in range(index + 1, len(items)):
            if items[i] < items[min_index]:
                min_index = i

        return min_index
