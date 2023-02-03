import random
list1=[]
for i in range(2):
   list1.append(random.randint(0,15))
print(list1)
computers_first_hand=random.randint(0,15)
print(f"computer's first hand is {computers_first_hand}")
computers_second_hand=random.randint(0,15)
a=input("Do you want to continue if yes write down y else n ")
def blackjack(b,c):
        
        if b<21 and  b>c and c<21:
            return "you win"
        elif b>21 and c>21 and b<c:
            return "you win"
    
        else:
            return "you lose"    
if a=="y":
    list1.append(random.randint(0,15))
    print(blackjack(sum(list1),computers_first_hand+computers_second_hand))
else:
    print(blackjack(sum(list1),computers_first_hand+computers_second_hand))