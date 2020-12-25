import time
import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hangman")
print(ascii_banner)
words =["car","window","aligator","bottle","teaandtech","gamingchair","stool"]

x=random.choice(words)

guesses = ''

name=input("Enter your name to begin the game: ")

time.sleep(0.5)
print("Hello",name,"and welcome to the game of hangman")

level=input("Select you difficulty level - easy, medium, hard: " )

maximum = 0
if level == 'hard' or level == 'Hard' or level == 'h' or level == "H":
    maximum=5
    print(maximum)

elif level == 'medium' or level == 'Medium' or level == 'm' or level == 'M':
    maximum=8

elif level == 'easy' or level == 'Easy' or level == 'e' or level == 'E':
    maximum=10

while maximum > 0:

    failed = 0

    for char in x:
        if char in guesses:
            print (char)

        else:

            print("_")
            failed += 1

    if failed == 0:
        print("You Won")
        break

    guess= input("Guess a character: ")

    guesses += guess

    if guess not in x:
            
        maximum -= 1

        print("Wrong, try another letter")

        if(maximum>1):
            print("You have",maximum,"turns left")
        elif(maximum==1):
            print("You have only",maximum,"turn left")
            
        elif maximum == 0:
            print("You lose")
