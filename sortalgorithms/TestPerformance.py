import time
from Utils import Utils
from BubbleSort import BubbleSort
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort

array_length = 10000


def performance(sort_algorithm):
    random_numbers = Utils.get_random_numbers_of_length(array_length)

    start_time = time.time()
    sort_algorithm.sort(random_numbers)
    elapsed_time = time.time() - start_time

    print("Time for sorting ", array_length, " elements with", sort_algorithm, "is: ",
          time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


performance(BubbleSort)
performance(SelectionSort)
performance(InsertionSort)
performance(MergeSort)
