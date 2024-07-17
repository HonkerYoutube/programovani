import random
ai_choice = random.randrange(1,3)
choice = input()

if ai_choice == 1:
    ai_choice = "rock"
if ai_choice == 2:
    ai_choice = "paper"
if ai_choice == 3:
    ai_choice = "scissors"


if choice == ai_choice:
    print(ai_choice)
    print(" ")
    print("it's draw")


elif choice == "rock" and ai_choice == "scissors":
    print(ai_choice)
    print(" ")
    print("you win")
elif choice == "scissors" and ai_choice == "paper":
    print(ai_choice)
    print(" ")
    print("you win")
elif choice == "paper" and ai_choice == "rock":
    print(ai_choice)
    print(" ")
    print("you win")


elif choice == "scissors" and ai_choice == "rock":
    print(ai_choice)
    print(" ")
    print("you lost")
elif choice == "rock" and ai_choice == "paper":
    print(ai_choice)
    print(" ")
    print("you lost")
elif choice == "paper" and ai_choice == "scissors":
    print(ai_choice)
    print(" ")
    print("you lost")