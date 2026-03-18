for i in range(6):
    for j in range(6):
        if j==0 or j==i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()