import random
a= random.randint(1,100)
print("Lets play the guess game")
c=1
while(c<7):
    print("Guess= ",c)
    guess= int(input("Please enter a number to guess: "))
    if(guess<a):
        print("Sorry guess too low")
    elif(guess>a):
        print("Sorry guess too high")
    elif(guess==a):
        print("Hurray!!! YOU WON")
        break;
    c=c+1
else:
    print("Sorry you lost. The number was= ",a)