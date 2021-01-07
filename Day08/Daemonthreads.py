import threading
import time

path = "text.txt"
text = ""

def readfile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readfile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()