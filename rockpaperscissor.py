import random
choices = ['r', 'p', 's']
while True:
    user_ch = input("choose one among the rock,paper,scissor (r/p/s): ")
    if user_ch not in choices:
        print("please enter a valid move")
    else:
        if user_ch == 'r':
            print("you have choosen rock")
        elif user_ch == 'p':
            print("you have choosen paper")
        else:
            print("you have choosen scissors")
    comp_ch = random.choice(choices)
    if comp_ch == 'r':
        print("computer have choosen rock")
    elif comp_ch == 'p':
        print("computer have choosen paper")
    else:
        print("computer have choosen scissors")

    if user_ch == 'r' and comp_ch == 's':
        print("you win..")
    elif user_ch == 'r' and comp_ch == 'p':
        print("computer win..")
    elif user_ch == 'r' and comp_ch == 'r':
        print("its a tie ...")
    elif user_ch == 'p' and comp_ch == 'r':
        print("you win..")
    elif user_ch == 'p' and comp_ch == 's':
        print("computer win..")
    elif user_ch == 'p' and comp_ch == 'p':
        print("its a tie..")
    elif user_ch == 's' and comp_ch == 'p':
        print("you win..")
    elif user_ch == 's' and comp_ch == 'r':
        print("computer win..")
    elif user_ch == 's' and comp_ch == 's':
        print("its a tie..")
    else:
        break
    should_continue = input("want to continue(y/n):")
    if should_continue.lower() != 'y':
        break
