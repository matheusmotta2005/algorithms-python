from sorting.interface import Sort

class Bubble(Sort):
    def __init__(self, input):
        self.arr = input

    def sort(self):
        # Sort a given array in ascending 
        # order using a basic bubble alg

        arr = self.arr
        arr_size = len(arr)
        for i in range(0, arr_size):
            for j in range(0, arr_size-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]