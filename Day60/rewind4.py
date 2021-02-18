""" Rewind 4
Recursion
"""
import pyfiglet
import queue
ascii_banner = pyfiglet.figlet_format("Rewind - 4")
print (ascii_banner)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
num = int(input("Enter a number to to find fibonacci series: "))
print(fib(num))

#FIFO
q = queue.Queue()
numbers = [10,20,30,40,50,60,70,80,90,100]
print("The Queue in FIFO order:")
for i in numbers:
    q.put(i)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

#LIFO
q2 = queue.LifoQueue()
numbers2=[20,40,60,80,100,120,140,160,180,200]
print("The Queue in LIFO order:")
for p in numbers2:
    q2.put(p)
print(q2.get())
print(q2.get())
print(q2.get())
print(q2.get())
print(q2.get())
print(q2.get())
print(q2.get())


#PriorityQueue
q3 = queue.PriorityQueue()
print("The Queue in Priority order:")
q3.put((2,"Shivam Bhosale"))
q3.put((3,"Computer Science Student"))
q3.put((1,"Data Scientist"))

while not (q3.empty()):
    print(q3.get())


def BinarySearch(arr,ele):
    first = 0
    last = len(arr) - 1
    index = -1

    while(first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == ele:
            index = mid
        elif ele < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return index

print("The number is found at array index: ",BinarySearch([10,20,30,40,50],40))





