def anagram_check(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    return sorted(s1) == sorted(s2)

print(anagram_check('Rise and Shine','Shine and Rise buddy')) 

import random
import time
import numpy as np
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
length=int(input("Enter the length of the input\n"))

def passgen(num):
    password = []
    for i in range (num):
        password.append(random.choice(chars))

    return np.unique(password)
print(passgen(length))


def bubblesort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i]> arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr

n = int(input("Enter the length of the array: "))
array = list(map(int,input("Enter the digits in the array: ").strip().split()))[:n]
print(bubblesort(array))

def LinearSearch(arr, ele):
    for i in range(len(arr)):
        if ele == arr[i]:
            return i+1
    return -1

n=int(input("Enter the length of the array: "))
a=list(map(int,input("Enter the elements in the array: ").strip().split()))[:n]
e=int(input("Enter the element to be searched: "))
print("Number found at array index: ",LinearSearch(a,e))


