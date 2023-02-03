import random
print("Welcome to Number Guessing Game ")
level=input("Which level do you want to try:- hard or easy ")
number=random.randint(0,5)
def guessing_game(guess):
        if guess<number:
            print("Too low")
            print("Try Again")
        elif guess>number:
            print("too high")
            print("Try again")
        elif guess==number:
            print("You got it")
            exit()
if level=="hard":
    count=5
    for i in range(5):
       
       guess= guessing_game(int(input("The number should be from 0 to 100")))
       count=count-1
    
else:
    for i in range(10):
       count=10
       guess= guessing_game(int(input("The number should be from 0 to 100")))
       count=count-1
if count==0 and guess!=number:
    print("You lost! Better Luck Next Time")






