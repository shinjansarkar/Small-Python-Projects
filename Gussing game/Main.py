import random
count=0
number=int(input("Enter a Number"))
Num = random.randint(0,10)
if Num ==number:
    print("You are correct")
    count=count+1

else:
    print("You are wrong")
print("Your number is",number)
print("Computer chose",Num)

print("point is ",count)