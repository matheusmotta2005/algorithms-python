def sort(arr):
    # Sort a given array in ascending order
    # using a divide-conquer merge algorithm
    arr_size = len(arr)
    if arr_size<2:
        return arr

    # Divide all array in left and right chunks
    mid = arr_size//2
    left = sort(arr[0:mid])
    right = sort(arr[mid:arr_size])

    # Start merging two chunked arrays into master array
    return mergeSort(arr,left,right)

def mergeSort(arr,left,right):
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
