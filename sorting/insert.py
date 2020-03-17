from sorting.interface import Sort

class Insert(Sort):
    def __init__(self, input):
        self.arr = input

    def sort(self):
        # Sort a given array in ascending 
        # order using a basic insert alg
        arr = self.arr
        arr_size = len(arr)

        for i in range(0, arr_size):
            j=i
            while j>0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j-=1