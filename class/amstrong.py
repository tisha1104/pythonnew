number=153
temp=number
sum=0
while number!=0:
    rem=number%10
    sum +=rem**3
    number=number//10
    
    
if sum==temp:
    print(f"{temp} is amstrong number")
else:
    #print(f"{temp} is not amstrong number")
    pass



# for i in range(100,1000):
#     number=i
#     temp=number
#     sum=0
#     while number !=0:
#         rem=number%10
#         sum += rem**3
#         number=number//10

#     if (sum==temp):
#          print(f"{temp} is amstrong number")
#     else:
#         # print(f"{temp} is not amstrong number")
#         pass