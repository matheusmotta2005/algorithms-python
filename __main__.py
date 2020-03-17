import sort
from log import Log
import config

input, log = [],Log([])

def reset(text):
    global input
    input = config.INPUT_ARRAY
    global log
    log = Log(input)
    print("===== "+str(text)+" =====")

# Bubble algorithm
# reset(input, log)
reset("Bubble Sort")
log.before()
sort.bubble(input)
log.after()

# Insert algorithm
reset("Insertion Sort")
log.before()
sort.insert(input)
log.after()

# Merge algorithm
reset("Merge Sort")
log.before()
sort.merge(input)
log.after()