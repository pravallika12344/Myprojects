import random
list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2=['1','2','3','4','5','6','7','8','9']
list3=['@','#','$','*','(',')','&','^','_']
a=int(input("how many letters do you want in the password"))
b=int(input("how many numbers do you want in the password"))
c=int(input("how many symbols do you want in password"))
i=0
output=[]
output1=''
if a+b+c<14:
    print("enter valid choices")
for j in range(1,a+1):
    output.append(random.choice(list1))
for j in range(1,b+1):
    output.append(random.choice(list2))
for j in range(1,c+1):
    output.append(random.choice(list3))
    i=i+1
random.shuffle(output)
for i in output:
    output1+=i
print(output1)