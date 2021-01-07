def LinearSearch(arr, ele):
    for i in range(len(arr)):
        if ele == arr[i]:
            return i
        
    return -1

n=int(input("Enter the length of the array: "))
a=list(map(int,input("Enter the elements in the array: ").strip().split()))[:n]
e=int(input("Enter the element to be searched: "))
print("Number found at array index: ",LinearSearch(a,e))