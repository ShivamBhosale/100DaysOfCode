import threading

event = threading.Event()

def myfunction():
    print("Waiting for event to trigger...")
    event.wait()
    print("Performing actions now..")

t1 =threading.Thread(target=myfunction)
t1.start()

x = input("\nDo you want to trigger the event (y/n)")
if x == "y": 
    event.set()

