import queue
import pyfiglet
#FIFO
ascii_banner = pyfiglet.figlet_format("Queues")
print(ascii_banner)
q = queue.Queue()
numbers=[10,20,30,40,50,60,70]
for i in numbers:
    q.put(i)
print(q.get())
print(q.get())
print(q.get())
print("\n")


#LIFO
q2 = queue.LifoQueue()
numbers2=[10,20,30,40,50,60,70]
for i in numbers2:
    q2.put(i)
print(q2.get())
print(q2.get())
print(q2.get())

#PriorityQueue
q3 = queue.PriorityQueue()

q3.put((2,"Shivam Bhosale"))
q3.put((3,"15-Nov-1999"))
q3.put((1, 21))

while not (q3.empty()):
    print(q3.get())



