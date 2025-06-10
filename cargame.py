#car game  
command=' '
started=True
stopped=False
print("if you dont know how to play the game, please enter help")
while command!="QUIT":
     command=input("> ").lower()
     if command=="start":
         if started:
             print("the car is already started")
         else:
             print("the car is started")
     elif command=="stop":
         if stopped:
             print("the car is already stopped")
         else:
             print("the car is stopped")
     elif command=="help":
        print('''start-to start the car
stop-to stop the car
quit-to quit the car''')
     elif command=="quit":
         quit()
     else:
         print("i didn't understand.")
