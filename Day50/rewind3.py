""" Since it is my 50th day of the 100DaysOfCode Challenge I have decided to go back and brush up my concepts """
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Rewind 3")
print(ascii_banner)
"""
def bubblesort(arr):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr

n=int(input("Enter the length of the array: "))
arr=list(map(int,input("Enter the element of the array: ").strip().split()))
print("Array before sorting: ",arr)
print("Array after sorting: ",bubblesort(arr))


def insertionSort(arr):
    for i in range(len(arr)-1):

        key = arr[i]
        j = i-1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr       

n=int(input("Enter the length of the array: "))
arr=list(map(int,input("Enter the element of the array: ").strip().split()))
print("Array before sorting: ",arr)
print("Array after sorting: ",insertionSort(arr))  


def LinearSearch(arr,ele):
    for i in range(1,len(arr)):
        if ele == arr[i]:
            return True
        else:
            return False

print(LinearSearch([10,20,30],20))
"""

def BinarySearch(arr,ele):
    first = 0
    last = len(arr)-1
    index = -1

    while(first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == ele:
            index = mid
        elif arr[mid] > ele:
            last = mid - 1
        else:
            first = mid + 1
    
    return index

print("The number is found at array index: ",BinarySearch([10,20,30,40,50],40))
        
        