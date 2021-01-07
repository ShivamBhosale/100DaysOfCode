import random
outcome =["Rock","Paper","Scissor"]
player_score = 0
Com_Score = 0
again="yes"
while(again == "yes" or again == "y"):
    a=input("Choose between Rock, Paper, and Scissor\n")
    x=random.choice(outcome)
    print("Computer Choose: ",x)
    if x == a:
        print("Draw")

    elif x == 'Rock' and a == 'Paper':
        print("Player Wins")
        player_score += 1

    elif x == "Paper" and a == "Rock":
        print("Computer Wins")
        Com_Score +=1

    elif x == "Scissor" and a == "Rock":
        print("Player Wins")
        player_score += 1

    elif x == "Rock" and a == "Scissor":
        print("Computer Wins")
        Com_Score +=1

    elif x == "Paper" and a == "Scissor":
        print("Player Wins")
        player_score += 1

    elif x == "Scissor" and a == "Paper":
        print("Computer Wins")
        Com_Score +=1

    again = "no"
    again = input("Do you want to play again:\n")
    
    if again == "no" or again == "n":
        print("Score:\n Computer = ",Com_Score,"\n","Player = ",player_score)

if (player_score>Com_Score):
    print("Player Wins the battle against the Computer")
elif (Com_Score>player_score):
    print("Computer Wins the Battle against the Player")
else:
    print("It's a Draw")