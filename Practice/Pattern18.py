n=6
for i in range(n):
    for j in range (2*n-1):
        if j==n-1-i or j==n-1+i or i==n-1:
            print(" *",end="")
        else:
            print(" ",end="")

        print()
# for j in range (5):
#         for i in range (5):
#             print("* ",end=" ")
#         print()