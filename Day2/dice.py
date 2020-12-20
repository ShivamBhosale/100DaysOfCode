import random
minimum = 1
maximum = 6
again ="yes"

while again =="yes" or again == "y":
    print("Dice is rolling....")
    x = random.randint(minimum,maximum)
    print(x)
    again="no"
    again = input("Roll Again y/n\n")