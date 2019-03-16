# ROCK || P{APER || SCISSOR

import random

#function defined for computer's choice


def computer():
    global computer_choice
    choice = ["Rock","Paper","Scissor"]
    selected = random.randint(0,2)
    computer_choice = choice[selected]
#function defined for person's choice
def person():
    global person_choice
    person_choice = input ("Rock, Paper, Scissor?? \n")

#function defined --> condition for winning
user_score = 0
computer_score = 0
def condition():
    global user_score
    global computer_score
    if (person_choice == computer_choice):
        print ("Its a Tie !!")
    elif (computer_choice == "Rock" and person_choice == "Paper"):
        print ("Player Wins!!")
        user_score += 1
    elif (computer_choice == "Rock" and person_choice == "Scissor"):
        print ("Computer Wins!!!")
        computer_score += 1
    elif (computer_choice == "Paper" and person_choice == "Scissor"):
        print ("Player Wins")
        user_score += 1
    elif (computer_choice == "Paper" and person_choice == "Rock"):
        print ("Compuiter Wins !!!")
        computer_score += 1
    elif (computer_choice == "Scissor" and person_choice == "Rock"):
        print ("PLayer Wins !!!")
        user_score += 1
    elif (computer_choice == "Scissor" and person_choice == "Paper"):
        print ("Computer Wins !!!")
        computer_score += 1


print ("\t\t\tROCK...PAPER....SCISSOR")
print ("Enter \"Exit\" to close")

while 1:
    print ("\n\n")
    person()
    if (person_choice == "Exit"):
        break
    computer()
    condition()
    print ("Player: ",user_score)
    print ("Computer: ",computer_score)
    
    


    
