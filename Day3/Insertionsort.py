"""Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards
in your hands. 
The array is virtually split into a sorted and an unsorted part.
Values from the unsorted part are picked and placed at the correct position in the sorted part.
-Source Geek fo Geeks"""
def insertionSort(arr):
    for i in range(1,len(arr)):
        
        key = arr[i]

        j= i-1
        while j>=0 and key < arr [j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
    return arr


n= int(input("Enter the number of elements in the array: "))
b = list(map(int,input("Enter the numbers : ").strip().split()))[:n]
print("The unsorted array is",b)
c=insertionSort(b)
print("The sorted array is",c)

#Time Complexity O(n^2)




