import random
def score(choice):
    system_choice = random.randint(1,3)
    if(choice>= 1 and choice <= 3):
        if(choice == system_choice):
            print("SYSTEM CHOICE = ",system_choice)
            print("BOTH OF YOU DIDN'T GET THE POINT!")
        elif(choice == 1 and system_choice == 2):
            print("SYSTEM CHOICE = ", system_choice)
            print("SYSTEM GET THE POINT!")
            return 0
        elif(choice == 2 and system_choice == 3):
            print("SYSTEM CHOICE = ", system_choice)
            print("SYSTEM GET THE POINT!")
            return 0
        elif(choice == 3 and system_choice == 1):
            print("SYSTEM CHOICE = ", system_choice)
            print("SYSTEM GET THE POINT!")
            return 0
        else:
            print("SYSTEM CHOICE = ", system_choice)
            print("YOU GET THE POINT!")
            return 1
    else:
        print("YOU ENTERED AN INCORRECT KEYSTROKE!")
user_score  = 0
system_score = 0
print("WELCOME TO ROCK,PAPER,SCISSORS GAME!")
while True:
    if(user_score == 3 or system_score == 3):
        if(user_score == 3):
            print("YOU WIN,CONGRATS!")
            break
        else:
            print("SYSTEM WIN!")
            break
    user_choice = int(input("\n1 --> ROCK\n"
          "2 --> PAPER\n"
          "3 --> SCISSORS\n"
          "MAKE YOUR CHOICE! "))
    winner = score(user_choice)
    if(winner == 1):
        user_score += 1
    if(winner == 0):
        system_score += 1
    print("\nYOUR SCORE = {}\nSYSTEM SCORE = {}".format(user_score,system_score))