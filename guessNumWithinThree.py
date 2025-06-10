secretnum=3
i=1
while i<=3:
    enternum=input("guess the number: ")  
    i+=1
    if str(secretnum)==str(enternum):
        print("your guess is correct.you won the game.")
        break
    else:
        print("your guess is wrong.please try again.")
if str(secretnum)!=str(enternum) and i>3:
    print("your chances are over.The secret number is : "+str(secretnum))
    