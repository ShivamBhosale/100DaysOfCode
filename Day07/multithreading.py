import threading

#Threading a technique which helps to excute multiple functions at the same time

def Name():
    for i in range(1000):
        print("My Name is Shivam Bhosale")

def Profession():
    for i in range(1000):
        print("I'm currently a CS undergrad")


t1 = threading.Thread(target=Name)
t2 = threading.Thread(target=Profession)

t1.start()
t2.start()
t1.join()
t2.join()


print("Another Text")