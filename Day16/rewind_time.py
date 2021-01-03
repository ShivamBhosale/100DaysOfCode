""" def anagram_check(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    
    return sorted(s1) == sorted(s2)

print(anagram_check('Rise and Shine','Shine and Rise buddy'))

#Method 2
def anagram_check(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    if(len(s1) != len(s2)):
        return False
    
    count={}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    
    return True

print(anagram_check("Johnny Walker","Walker Nonjhy")) 

import random
import time
import numpy as np
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
length=int(input("What should be the length of your password?\n"))
def pass_gen(num):
    password = []
    for i in range(num):
        password.append(random.choice(chars))
    return np.unique(password)
print(pass_gen(length)) 


def bubblesort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr
n=int(input("Enter the length of the array: "))
array=list(map(int,input("Enter the array to be sorted: ").strip().split()))[:n]
print(bubblesort(array)) 

def insertionSort(arr):
    for i in range(1,len(arr)):

        key = arr[i] 

        j = i - 1
        while j>=0 and key < arr [j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr 
n=int(input("Enter the length of the array: "))
array=list(map(int,input("Enter the array to be sorted: ").strip().split()))[:n]
print(insertionSort(array))

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
        
        if i>= j:
            return j
        num[i], num[j] = num[j], num[i]

def quick_sort(num):
    def quick_sort2(items,low,high):
        if low < high:
            split_index = partition(items, low, high)
            quick_sort2(items,low,split_index)
            quick_sort2(items,split_index+1,high)
    quick_sort2(num,0,len(num)-1)
    return num
    
n=int(input("Enter the length of the array: "))
array=list(map(int,input("Enter the array to be sorted: ").strip().split()))[:n]
print(quick_sort(array))  """

def selection_sort(arr):
    for i in range(len(arr)):
        l_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[l_index]:
                l_index = j
        arr[i], arr[l_index] = arr[l_index], arr[i]
    return arr
n=int(input("Enter the length of the array: "))
array=list(map(int,input("Enter the array to be sorted: ").strip().split()))[:n]
print(selection_sort(array))




    




