"""Quick Sort begins by partitioning the list -
Picking one value of the list that will be in its sorted place.
This value is called a pivot. All elements smaller than the pivot are moved to its left.
All larger elements are moved to its right.
Knowing that the pivot is in it's rightful place,
We recursively sort the values around the pivot until the entire list is sorted. """

def partition(num,low,high):
    pivot = num[(low+high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while num[i] < pivot:
            i += 1
        j -= 1
        while num[j] > pivot:
            j -= 1
        if i >= j:
            return j

        num [i], num [j] = num[j], num[i]

def quick_sort(num):
    def quick_sort2(items,low,high):
        if low < high:
            split_index = partition(items,low,high)
            quick_sort2(items,low,split_index)
            quick_sort2(items,split_index + 1, high)
    quick_sort2(num,0,len(num)-1)
    return num

n=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements in the array: ").strip().split()))[:n]
print("Array before the quick sort: ",a)
print("Array after the quick sort:",quick_sort(a))