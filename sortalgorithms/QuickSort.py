from Utils import Utils
from Stack import Stack


class QuickSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(items):
        stack = Stack()
        stack.push(0)
        stack.push(len(items) - 1)

        while not stack.is_empty():
            end_index = stack.pop()
            start_index = stack.pop()

            partition_element_index = QuickSort.__partition(items, start_index, end_index)

            if partition_element_index - 1 > start_index:
                stack.push(start_index)
                stack.push(partition_element_index - 1)

            if partition_element_index + 1 < end_index:
                stack.push(partition_element_index + 1)
                stack.push(end_index)

        return items

    @staticmethod
    def __partition(items, start_index, end_index):
        i = start_index + 1
        j = end_index

        while True:

            while items[i] < items[start_index]:
                i += 1
                if i == end_index:
                    break

            while items[start_index] < items[j]:
                j -= 1
                if j == start_index:
                    break

            if i >= j:
                break
            Utils.swap(items, i, j)

        Utils.swap(items, start_index, j)
        return j
