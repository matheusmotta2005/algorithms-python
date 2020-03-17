from sorting.interface import Sort

class Merge(Sort):
    def __init__(self, input):
        self.arr = input

    def sort(self):
        # Use a private mergeSplit logic to divide array in small chunks using recursion
        # as Sort interface has no paremeters to recursive
        self.__mergeSplit(self.arr)
    
    def __mergeSplit(self, arr):
        arr_size = len(arr)

        # Stop chunking array when minimum size was reached
        if arr_size<2:
            return arr

        # Divide array in the middle to compare left and right chunks
        mid = arr_size//2
        left = arr[0:mid]
        right = arr[mid:arr_size]

        # Start merging two minimum chunked arrays into a master array
        return self.__mergeSort(arr, self.__mergeSplit(left), self.__mergeSplit(right))

    def __mergeSort(self, arr, left, right):
        i,l,r = 0,0,0
        left_size = len(left)
        right_size = len(right)

        # Given a left and right arrays sort them
        # using a small value priority
        while l<left_size and r<right_size:
            if left[l] < right[r]:
                arr[i] = left[l]
                l+=1
            else:
                arr[i] = right[r]
                r+=1
            i+=1
        
        # Add unbalanced high
        # values of left array
        # to main sorted array
        while l<left_size:
            arr[i] = left[l]
            l+=1
            i+=1
        
        # Add unbalanced high
        # values of right array
        # to main sorted array
        while r<right_size:
            arr[i] = right[r]
            r+=1
            i+=1

        return arr