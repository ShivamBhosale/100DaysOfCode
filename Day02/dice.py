import random
import time
minimum = 1
maximum = 6
again ="yes"

while again =="yes" or again == "y":
    print("Dice is rolling....")
    x = random.randint(minimum,maximum)
    time.sleep(1)
    print(x)
    again = input("Roll Again y/n \n")
time.sleep(1)
if again == 'no' or 'n':
    print("Thanks for playing")