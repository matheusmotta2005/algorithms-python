import sort, config
from datetime import datetime
from log import Log

input, log = [],Log([])

def reset(text):
    global input
    input = config.INPUT_ARRAY[:]
    global log
    log = Log(input)
    print("===== "+str(text)+" =====")

# Bubble algorithm
# reset(input, log)
reset("Bubble Sort")
sort.bubble(input)

# Insert algorithm
reset("Insertion Sort")
sort.insert(input)

# Merge algorithm
reset("Merge Sort")
sort.merge(input)

# QuickSOrt algorithm
reset("Quick Sort")
sort.quick(input)