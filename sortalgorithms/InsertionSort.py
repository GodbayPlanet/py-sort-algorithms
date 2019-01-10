from Utils import Utils


class InsertionSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(items):
        for i in range(0, len(items)):
            for j in range(i, 0, -1):
                if items[j] < items[j - 1]:
                    Utils.swap(items, j, j - 1)
                else:
                    break

        return items


numbers = Utils.get_numbers()
print("Unsorted numbers", numbers)
print("Sorted numbers", InsertionSort.sort(numbers))
