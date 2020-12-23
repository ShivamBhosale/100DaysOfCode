def BinarySearch(arr,ele):
    first = 0
    last = len(arr)-1
    index = -1
    
    while (first <= last ) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == ele:
            index = mid
        elif ele < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return index

print("The number is found at array index: ",BinarySearch([10,20,30,40,50],40))