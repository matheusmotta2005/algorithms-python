class Binary:
    # Set a global counter of search executions
    __searchCount = 0

    def search (self, arr, num):
        # Count search executions
        self.__searchCount+=1 

        arr_size = len(arr)
        if arr_size < 1:
            return False
        if arr_size == 1:
            return num == arr[0] 
       
        # When element is on the middle or array size 1
        mid = arr_size//2
        if num == arr[mid]:
            return True
        # When searching element is greatter than mid element
        # execute another binary search from middle to end 
        # otherwise execute from beginning to middle
        if num > arr[mid]:
            return self.search(arr[mid:arr_size], num)
        else:
            return self.search(arr[0:mid], num)
    
    def getSearchDepth(self):
        # Retrieve the depth search count
        return self.__searchCount