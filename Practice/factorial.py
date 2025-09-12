#===============================foor loop====================================
num=int(input("Enter the number:"))
fact=1
for i in range (1,num+1):
    fact=fact*i
    print(f"Factorial of",{num},"is:",{fact})
    

#===============================While loop===================================
num=int(input("Enter the number:"))
fact=1
i=1
while i<=num:
    fact =fact*i
    i = i+1
print(f"Factorial of",{num},"is:",{fact})