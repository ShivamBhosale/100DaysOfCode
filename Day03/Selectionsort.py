"""This algorithm segments the list into two parts: sorted and unsorted.
We continuously remove the smallest element of the unsorted segment of the list
and append it to the sorted segment. - Source Stackabuse"""

def selection_sort(arr):
    for i in range(len(arr)):
        l_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[l_index]:
                l_index = j

        arr[i], arr[l_index] = arr[l_index], arr[i]

    return arr

n=int(input("Enter the total number of elements in the array: "))
a=list(map(int,input("Enter the elements in the array: ").strip().split()))[:n]
print("Array before the selection sort: ",a)
print("Array after the selection sort: ",selection_sort(a))