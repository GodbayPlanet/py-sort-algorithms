class BubbleSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(items):
        for i in range(0, len(items) - 1):
            for j in range(0, len(items) - i - 1):
                if BubbleSort.__is_less(items[j + 1], items[j]):
                    BubbleSort.__swap(items, j + 1, j)
        return items

    @staticmethod
    def __is_less(item_one, item_two):
        return item_one < item_two

    @staticmethod
    def __swap(items, i, j):
        temp = items[i]
        items[i] = items[j]
        items[j] = temp


numbers = [4, 3, 2, 1]

print("Unsorted numbers", numbers)

print("Sorted numbers", BubbleSort.sort(numbers))

characters = ['f', 'b', 'a', 'd', 'h', 'c']

print("Unsorted characters", characters)

print("Sorted characters", BubbleSort.sort(characters))
