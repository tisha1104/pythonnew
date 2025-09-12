for i in range(5):
    for j in range(5):
        if j==0 or j==5-1 or i==5//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

