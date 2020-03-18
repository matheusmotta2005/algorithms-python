from searching.binary import Binary
from searching.sequential import Sequential

class Search:
    def __init__(self, input):
        self.__input = input
    
    def binarySearch(self, num):
        print("===== Binary Search =====")
        binary = Binary()
        result = binary.search(self.__input, num)
        self.__printResult(result)
        print("Search dept: "+str(binary.getSearchDepth()))
    
    def sequential(self, num):
        print("==== Sequential Search =====")
        sequential = Sequential()
        result = sequential.search(self.__input, num)
        self.__printResult(result)

    def __printResult(self, result):
        if result:
            print("Found it!")
        else:
            print("Not found.")