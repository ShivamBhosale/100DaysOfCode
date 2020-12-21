"""We begin by comparing the first two elements of the list.
If the first element is larger than the second element, we swap them.
If they are already in order we leave them as is. We then move to the next pair of elements,
compare their values and swap as necessary. This process continues to the last pair of 
items in the list"""

def bubblesort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # Swap the elements
                arr [i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr

n=int(input("Enter the number of elements in the array: "))
a= list(map(int,input("Enter the elements in the array: ").strip().split()))[:n]
print("Array before sorting: ",a)

print("Array after bubble sort:",bubblesort(a))