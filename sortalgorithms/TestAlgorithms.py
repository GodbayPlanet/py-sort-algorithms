from Utils import Utils
from QuickSort import QuickSort
from MergeSort import MergeSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from BubbleSort import BubbleSort

# QUICK SORT

print("----- QUICK SORT -----\n")

numbers = Utils.get_numbers()
print("Unsorted numbers", numbers)
print("Sorted numbers", QuickSort.sort(numbers))

characters = Utils.get_characters()
print("Unsorted characters", characters)
print("Sorted characters", QuickSort.sort(characters))

strings = Utils.get_strings()
print("Unsorted strings", strings)
print("Sorted stirngs", QuickSort.sort(strings))

# MERGE SORT
print("\n----- QUICK SORT -----\n")

numbers = Utils.get_numbers()
print("Unsorted numbers", numbers)
print("Sorted numbers", MergeSort.sort(numbers))

characters = Utils.get_characters()
print("Unsorted characters", characters)
print("Sorted characters", MergeSort.sort(characters))

# INSERTION SORT
print("\n----- INSERTION SORT -----\n")

numbers = Utils.get_numbers()
print("Unsorted numbers", numbers)
print("Sorted numbers", InsertionSort.sort(numbers))

characters = Utils.get_characters()
print("Unsorted characters", characters)
print("Sorted characters", InsertionSort.sort(characters))

# SELECTION SORT
print("\n----- SELECTION SORT -----\n")

numbers = Utils.get_numbers()
print("Unsorted numbers", numbers)
print("Sorted numbers", SelectionSort.sort(numbers))

characters = Utils.get_characters()
print("Unsorted characters", characters)
print("Sorted characters", SelectionSort.sort(characters))

strings = Utils.get_strings()
print("Unsorted string", strings)
print("Sorted strings", SelectionSort.sort(strings))

# BUBBLE SORT
print("\n----- BUBBLE SORT -----\n")

numbers = Utils.get_numbers()
print("Unsorted numbers", numbers)
print("Sorted numbers", BubbleSort.sort(numbers))

characters = Utils.get_characters()
print("Unsorted characters", characters)
print("Sorted characters", BubbleSort.sort(characters))
