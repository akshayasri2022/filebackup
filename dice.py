# ask user if he want to play or not
# roll the dice and give 2 random numbers
# if not terminate

import random
while True:
    choice = input("do you want to roll the dice? (y/n)  ")
    if choice.lower() == "y":
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        print(f"the numbers are {r1},{r2}")
    elif choice.lower() == "n":
        print("see you again...")
        break
    else:
        print("invalid choice")
        break
