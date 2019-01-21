from Utils import Utils


class MergeSort:

    def __init__(self):
        pass

    @staticmethod
    def sort(items):
        i = 1
        while i <= len(items) - 1:
            j = 0
            while j < len(items) - 1:
                mid = j + i - 1
                right_end = min(j + 2 * i - 1, len(items) - 1)

                MergeSort.__merge(items, j, mid, right_end)
                j = j + i * 2

            i = 2 * i
        return items

    @staticmethod
    def __merge(items, left_start, mid, right_end):
        aux = list(items)

        i = left_start
        j = mid + 1
        k = left_start

        while k <= right_end:
            if i > mid:
                items[k] = aux[j]
                j += 1
            elif j > right_end:
                items[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                items[k] = aux[j]
                j += 1
            else:
                items[k] = aux[i]
                i += 1
            k += 1
