# Print numbers from 1 to 10 without using range(1,11)

# i=0
# while i!=12:
#     print(i)
#     i+=1
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# Print numbers from 1 to 10 using for
# for i in range(1,21):
#     if i%2==0:
#         print(i)
# Take a number and print its table
# num=int(input("Enter The Number:- "))

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")
    
# print("==============================================================")    

# num=int(input("Enter Number :- "))
# total=0
# for i in range(1,num+1):
#     total+=i
# print(total)

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

# Reverse a number
num=input("Enter The Number:- ")
rev_num=""
# rev_num=num[::-1]
# print(rev_num)

for i in num:
    rev_num=i+rev_num
print(rev_num)