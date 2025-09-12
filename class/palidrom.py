number = 12345654321
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum = sum*10 +rem
    numbe = number//10

if (sum==temp):
    print(f"{temp} is palidrom number")
else :
    print(f"{temp} is not palidrom number")