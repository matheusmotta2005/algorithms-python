import sort
from config import *

def reset(text):
    global input
    input = INPUT_ARRAY[:]
    print("===== "+str(text)+" =====")

def main():
    if SORT_BUBBLE_ENABLED:
        # Bubble algorithm
        reset("Bubble Sort")
        sort.bubble(input)

    if SORT_INSERT_ENABLED:
        # Insert algorithm
        reset("Insertion Sort")
        sort.insert(input)

    if SORT_MERGE_ENABLED:
        # Merge algorithm
        reset("Merge Sort")
        sort.merge(input)

    if SORT_QUICK_ENABLED:
        # QuickSOrt algorithm
        reset("Quick Sort")
        sort.quick(input)
main()