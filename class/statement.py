#=======================================conditional statment=====================================
#=======================================if-else,if,nasted-if=====================================
# age=17
# if age>=18:
#     print("you are eligebale for voting")
# else:
#     print("you are not eligebale for voting")

a=100
b=15
c=89
# if a>b:
#     print(" a is greater")
# else:
#     print(" b is greater")
# if a>b :
#     if a>c:
#         print(" a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater") 
else:
    print("c is greater")