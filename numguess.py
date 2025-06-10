import random
num = random.randint(1, 100)
while True:
    try:
        guess = int(input("guess the number:"))
        if guess < num:
            print("too low")
        elif guess == num:
            print("you guessed the number right")
            break
        else:
            print("too high")
    except NameError and ValueError:
        print("please enter a valid number")
