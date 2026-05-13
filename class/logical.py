


# number = 12345654321
# temp = number
# sum = 0
# while number!=0:
#     rem = number%10
#     sum = sum*10 +rem
#     number = number//10

# if (sum==temp):
#     print(f"{temp} is palidrom number")
# else :
#     print(f"{temp} is not palidrom number") 

# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()


print("====================================================================================")

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()       

print("====================================================================================")
#              *
#            * *
#          * * *
#        * * * *
#      * * * * *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("====================================================================================")

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
print("====================================================================================")

#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print("====================================================================================")


# * * * * *
# *       *
# *       *
# *       *
# * * * * *
for i in range(6):
    for j in range(6):
        if i==0 or j==0 or i==5 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("====================================================================================")

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("====================================================================================")


#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(2,7):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print("====================================================================================")

#           *
#         * * *
#        * * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print("====================================================================================")

# *                     *
# * *                 * *
# * * *             * * *
# * * * *         * * * *
# * * * * *     * * * * *
# * * * * * * * * * * * *
# * * * * * * * * * * * *
# * * * * *     * * * * *
# * * * *         * * * *
# * * *             * * *
# * *                 * *
# *                     *
for i in range(1,6+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(6-i)):
        print(" ",end=" ")
    for a in range(i):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(6-i)):
        print(" ",end=" ")
    for a in range(i):
        print("*",end=" ")
    print()

print("====================================================================================")

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *
for i in range(6):
    for j in range(6):
        if j==0 or j==i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("====================================================================================")

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("====================================================================================")

# * * * * * *
# *       *
# *     *
# *   *
# * *         
# *
for i in range(6):
    for j in range(6):
        if i==0 or j==0 or j==6-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("====================================================================================")
#           * 
#         *   * 
#       *       * 
#     *           * 
#   *               * 
#   *               * 
#     *           * 
#       *       * 
#         *   * 
#           * 
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(5,0,-1):
        for k in range(6-i):
            print(" ",end=" ")
        for j in range(2*i-1):
            if j==0 or j==2*i-2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
print("====================================================================================")
# A 
# B C 
# D E F 
# G H I J 
ch=1
for i in range(1,5):
    for j in  range(i):
        print(chr(64+ch),end=" ")
        ch+=1
    print()
print("====================================================================================")
# a 
# b c 
# d e f 
# g h i j 
ch=1
for i in range(1,5):
    for j in  range(i):
        print(chr(96+ch),end=" ")
        ch+=1
    print()
print("====================================================================================")
# G H I J 
# D E F 
# B C 
# A 
ch=10
for i in range(4,0,-1):
    start=ch-i+1
    for j in range(start,ch+1):
        print(chr(64+j),end=" ")
    print()
    ch-=i
print("====================================================================================")
# A 
# B B 
# C C C 
# D D D D 
for i in range(1,5):
    for j in range(i):
        print(chr(64+i),end=" ")
        ch+=1
    print()
# print("====================================================================================")
