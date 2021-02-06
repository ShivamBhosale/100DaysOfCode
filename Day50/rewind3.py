""" Since it is my 50th day of the 100DaysOfCode Challenge I have decided to go back and brush up my concepts """
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Rewind 3")
print(ascii_banner)

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
        

class Person:
    amount = 0
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        Person.amount += 1

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Weight {self.weight}")


x =  Person("Shivam",21,64)
print(x)


y = Person("Sunil",54,89)
print(y)

print(Person.amount)


class Player:

    count = 0
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        Player.count += 1

    def __str__(self):
        return (f"Name:{self.name}, Age:{self.age}, Height:{self.height}")

    def get_older(years):
        self.age += years
    
# Inheritance
class Stats(Player):

    def __init__(self,name,age,height,position):
        super(Stats,self).__init__(name,age,height)
        self.position = position

    def __str__(self):
        text = super(Stats,self).__str__()
        text += ", Position: {}".format(self.position)
        return text
    

Player1 = Stats("Shivam",21,156,"Mid-Field")
print(Player1)


# Recursion

def fact(n):
    
    if n < 1:
        return 1
    
    else:
        number = n * fact(n-1)
        return number
a = int(input("Enter an integer to find the factorial: "))
print(fact(a))

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        number = fib(n-1) + fib(n-2)
        return number

a = int(input("Enter a number to find the fib number: "))
print(fib(a))


