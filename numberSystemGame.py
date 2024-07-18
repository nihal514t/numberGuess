import random
#computer guess some numbers between 1-10
x=random.randint(1,10)

#display to user for input
y=int(input("Enter Your Guess :"))

#its check the value of userInput and computer Guess 
# then print a corresponding message 
if(x==y):
    print("Congratz! Correct Number:",x,"\ncomputer guessed",x)
else: 
    print("You Are Failed","\nComputer Guessed :",x)
