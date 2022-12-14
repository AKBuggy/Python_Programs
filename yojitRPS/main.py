import random
import os

val = True


def fetch_userschoice():
    print("\nEnter your choice:\n1: Rock\n2: Paper\n3: Scissors\n4: Quit\n")
    userschoice = int(input("User's choice = "))
    return userschoice


def fetch_machinechoice():
    machinechoice = random.randint(1, 3)
    return machinechoice


def compare_choices(userschoice, machinechoice):
    if userschoice == 1 and machinechoice == 2:
        print("Machine Wins!!")
        save_scores("Rock", "Paper", "Machine Wins")
    elif userschoice == 2 and machinechoice == 3:
        print("Machine Wins")
        save_scores("Paper", "Scissors", "Machine Wins")
    elif userschoice == 3 and machinechoice == 1:
        print("Machine Wins")
        save_scores("Scissors", "Rock", "Machine Wins")

    elif userschoice == 2 and machinechoice == 1:
        print("User Wins")
        save_scores("Paper", "Rock", "User Wins")
    elif userschoice == 3 and machinechoice == 2:
        print("User Wins")
        save_scores("Scissors", "Paper", "User Wins")
    elif userschoice == 1 and machinechoice == 3:
        print("User Wins")
        save_scores("Rock", "Scissors", "User Wins")

    else:
        print("Draw")


def save_scores(userschoice, machinechoice, outcome):
    filename = "scores.csv"
    try:
        f = open(filename, 'r')
        f = open(filename, 'a')
        f.write('\n' + userschoice + ',' + machinechoice + ',' + outcome)
        f.close
    except:
        f = open(filename, 'w')
        f.write("Userchoice," + "Machinechoice," + "Outcome")


while val:
    userschoice = fetch_userschoice()

    if userschoice == 4:
        val = False
        break

    elif userschoice > 0 and userschoice < 5:
        machinechoice = fetch_machinechoice()
        print("Machine's choice =", machinechoice)
        compare_choices(userschoice, machinechoice)

    else:
        print("Plese enter a valid option.")