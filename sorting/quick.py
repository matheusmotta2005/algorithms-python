from sorting.interface import Sort

class Quick(Sort):
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        # Use a private quick sort method as we need recursion with range
        # and Sort interface requires a simple sort function
        self.__quickSort(self.arr, 0, len(self.arr)-1)

    def __quickSort(self, arr, start, end):
        if start < end:
            # Identify last pivot index
            pIndex = self.__pivot(arr, start, end)
            # Sort left side of pivot
            self.__quickSort(arr, start, pIndex-1)
            # Sort right side of pivot
            self.__quickSort(arr, pIndex+1, end)

    def __pivot(self, arr, start, end):
        # Use last index as pivot
        pivot = arr[end]
        # Define lowest index as before start
        min = start-1
        
        for i in range(start, end):
            if(arr[i] < pivot):
                min+=1
                arr[min], arr[i] = arr[i], arr[min]

        arr[min+1], arr[end] = arr[end], arr[min+1]

        return (min+1)