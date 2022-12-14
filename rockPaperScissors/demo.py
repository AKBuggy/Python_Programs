import random


# ----------------------------------
def fetch_userschoice():
    print("Enter your choice:\n 1 rock \n 2 paper \n 3 scissors")
    isValid = False

    while not isValid:
        try:
            users_choice = int(input("Man = "))
            if users_choice >= 1 and users_choice <= 3:
                isValid = True
            else:
                print('Select the number from the above given choices')
        except:
            print('Select the number from the above given choices')

    return users_choice


# ----------------------------------
def fetch_machchoice():
    mach_choice = random.randint(1, 3)
    return mach_choice


# ----------------------------------
def fetch_outcome(users_choice, mach_choice):
    if users_choice == mach_choice:
        outcome = "It's a draw"
    elif users_choice == 1 and mach_choice == 3 or users_choice > mach_choice:
        outcome = "Man wins"
    else:
        outcome = "Machine wins"
    return outcome


# ----------------------------------

def save_scores(count, users_choice, mach_choice, outcome):
    file_name = "Scores.txt"
    # fetch handle to the file
    f = open(file_name, 'a')
    exist = open(file_name, 'r').read()
    header = "Round, " + "\t" + "your choice, " + "\t" + "machine's choice, " + "\t" + "result" + "\t \n"

    if exist == '':
        f.write(header)

    temp = str(count) + ",\t\t" + str(users_choice) + ",\t\t" + str(mach_choice) + ",\t\t" + outcome + "\t\t\t\t \n"

    f.write(temp)
    f.close()


# ----------------------------------
if __name__ == '__main__':
    print("Let the game begins")
    flag = True
    count = 0
    while flag:
        count = count + 1
        users_choice = fetch_userschoice()  # users_choice function call
        print("Your choice was:", users_choice)
        mach_choice = fetch_machchoice()  # mach_choice function call
        print("Machine's choice was:", mach_choice)
        outcome = fetch_outcome(users_choice, mach_choice)
        print(outcome)
        save_scores(count, users_choice, mach_choice, outcome)

        print("Do you want to continue the game: press 1 for yes and any number for no")
        contiExit = int(input())
        if contiExit == 1:
            continue
        else:
            print("Thank You for playing")
            exit()
